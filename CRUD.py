import MySQLdb as mdb
import sys

def createDB():
    try:
        con = mdb.connect('localhost', 'user', 'goodPassword', 'league');

        cur = con.cursor()

        #Criando tabela jogador
        #cur.execute("DROP TABLE IF EXISTS jogador")
        cur.execute("CREATE TABLE `jogador` ( \
                      `jogador_id` int(11) NOT NULL,\
                      `time_id` int(11) DEFAULT NULL,\
                      `nome` varchar(45) DEFAULT NULL,\
                      `abates_totais` int(11) DEFAULT NULL,\
                      `mortes_totais` int(11) DEFAULT NULL\
                    ) ENGINE=MyISAM DEFAULT CHARSET=latin1;")

        #Criando tabela partida
        #cur.execute("DROP TABLE IF EXISTS partida")
        cur.execute("CREATE TABLE `partida` (\
                      `partida_id` int(11) NOT NULL,\
                      `timeA_id` int(11) DEFAULT NULL,\
                      `timeB_id` int(11) DEFAULT NULL,\
                      `abates_timeA` int(11) DEFAULT NULL,\
                      `abates_timeB` int(11) DEFAULT NULL,\
                      `vencedor_id` int(11) DEFAULT NULL,\
                      `torneio_id` varchar(45) DEFAULT NULL\
                    ) ENGINE=MyISAM DEFAULT CHARSET=latin1;")

        #Criando tabela personagem
        #cur.execute("DROP TABLE IF EXISTS personagem")
        cur.execute("CREATE TABLE `personagem` (\
                      `personagem_id` int(11) NOT NULL,\
                      `personagem_nome` varchar(45) DEFAULT NULL,\
                      `personagem_preco` int(11) DEFAULT NULL\
                    ) ENGINE=MyISAM DEFAULT CHARSET=latin1;")

        #Criando tabela personagem_comprado
        #cur.execute("DROP TABLE IF EXISTS personagem_comprado")
        cur.execute("CREATE TABLE `personagem_comprado` (\
                      `personagem_id` int(11) NOT NULL,\
                      `jogador_id` int(11) DEFAULT NULL\
                    ) ENGINE=MyISAM DEFAULT CHARSET=latin1;")

        #Criando tabela time
        #cur.execute("DROP TABLE IF EXISTS time")
        cur.execute("CREATE TABLE `time` (\
                      `time_id` int(11) NOT NULL,\
                      `nome_time` varchar(45) DEFAULT NULL,\
                      `abates` int(11) DEFAULT NULL,\
                      `mortes` int(11) DEFAULT NULL\
                    ) ENGINE=MyISAM DEFAULT CHARSET=latin1;")

        #Criando tabela torneio
        #cur.execute("DROP TABLE IF EXISTS torneio")
        cur.execute("CREATE TABLE `torneio` (\
                      `torneio_id` int(11) NOT NULL,\
                      `regiao_torneio` varchar(45) DEFAULT NULL\
                    ) ENGINE=MyISAM DEFAULT CHARSET=latin1;")

        #Criando relacionamentos
        cur.execute("ALTER TABLE `jogador`\
                      ADD PRIMARY KEY (`jogador_id`);")

        cur.execute("ALTER TABLE `partida`\
                      ADD PRIMARY KEY (`partida_id`);")

        cur.execute("ALTER TABLE `personagem`\
                      ADD PRIMARY KEY (`personagem_id`);")

        cur.execute("ALTER TABLE `personagem_comprado`\
                      ADD KEY `jogador_id` (`jogador_id`),\
                      ADD KEY `jogador_id_2` (`jogador_id`);")

        cur.execute("ALTER TABLE `time`\
                      ADD PRIMARY KEY (`time_id`);")

        cur.execute("ALTER TABLE `torneio`\
                      ADD PRIMARY KEY (`torneio_id`);")

        cur.execute("ALTER TABLE `jogador`\
                      MODIFY `jogador_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;")

        cur.execute("ALTER TABLE `partida`\
                      MODIFY `partida_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;")

        cur.execute("ALTER TABLE `personagem`\
                      MODIFY `personagem_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;")

        cur.execute("ALTER TABLE `time`\
                      MODIFY `time_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;")
    except mdb.Error as e:

        print("Error %d: %s" % (e.args[0],e.args[1]))
        sys.exit(1)

    finally:

        if con:
            con.close()

def readTables(option: int):
    try:
        con = mdb.connect('localhost', 'user', 'goodPassword', 'league');

        cur = con.cursor()

        cur.execute("SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")

        if option == 0:
            #View - Atualmente qual o time vencedor? Considere o total de vitorias como o primeiro paramentro, caso empate, o total de abates, caso empate de novo, o que tiver menos mortes
            cur.execute("SELECT time.nome_time AS Vencedor FROM partida\
                        JOIN time\
                        ON time.time_id = partida.vencedor_id\
                        GROUP BY time.time_id\
                        ORDER BY COUNT(*)DESC, time.abates DESC,\
                        time.mortes ASC LIMIT 1")
        if option == 1:
            #Consulta 1 - Qual o personagem mais comprado do jogo?
            cur.execute("SELECT personagem.personagem_nome AS Personagem, COUNT(personagem_comprado.personagem_id) AS Quantia FROM personagem_comprado\
                        JOIN personagem\
                        ON personagem.personagem_id = personagem_comprado.personagem_id\
                        GROUP BY personagem_comprado.personagem_id\
                        ORDER BY Quantia DESC LIMIT 1 ")
        if option == 2:
            #Consulta 2 - Quais personagens o jogador de id == 1 possui?
                cur.execute("SELECT personagem.personagem_nome FROM personagem\
                            JOIN personagem_comprado\
                            ON personagem_comprado.personagem_id = personagem.personagem_id\
                            WHERE personagem_comprado.jogador_id = 1")
        if option == 3:
            #Consulta 3 - Qual jogador possui mais personagens?
            cur.execute("SELECT jogador.nome, COUNT(personagem_comprado.jogador_id) AS Quantidade FROM personagem_comprado\
                        JOIN jogador\
                        ON jogador.jogador_id = personagem_comprado.jogador_id\
                        GROUP BY personagem_comprado.jogador_id\
                        ORDER BY Quantidade DESC LIMIT 1\
                        ")
        if option == 4:
            #Consulta 4 - Mostre o jogador com mais abates de cada time
            cur.execute("SELECT f.nome, time.nome_time, f.abates_totais\
                        FROM (\
                           SELECT jogador.nome, jogador.time_id, max(jogador.abates_totais) AS minprice\
                           FROM jogador GROUP BY jogador.time_id\
                        ) AS x INNER JOIN jogador AS f ON f.time_id = x.time_id AND f.abates_totais = x.minprice\
                        JOIN time\
                        ON time.time_id = f.time_id")
        if option == 5:
            #Consulta 5 - Mostre todos os jogadores, seus abates e mortes do time de nome BepidPower
            cur.execute("SELECT time.nome_time, jogador.nome, jogador.abates_totais AS Abates, jogador.mortes_totais AS Mortes FROM time\
                        JOIN jogador\
                        ON time.time_id = jogador.time_id\
                        WHERE time.nome_time = 'BepidPower' \
                        ")

        for row in cur.fetchall():
            print(row)


    except mdb.Error as e:

        print("Error %d: %s" % (e.args[0],e.args[1]))
        sys.exit(1)

    finally:

        if con:
            con.close()

def insertRows():
     try:
        con = mdb.connect('localhost', 'user', 'goodPassword', 'league');

        cur = con.cursor()

        #Inserindo jogadores
        cur.execute("INSERT INTO `jogador` (`jogador_id`, `time_id`, `nome`, `abates_totais`, `mortes_totais`) VALUES\
                    (1, 1, 'Italus', 5, 2),\
                    (2, 1, 'Thiago', 10, 7),\
                    (3, 1, 'Gabriela', 1, 3),\
                    (4, 1, 'Macabeus', 0, 3),\
                    (5, 1, 'Trabson', 14, 0),\
                    (6, 2, 'Douglas', 8, 8),\
                    (7, 2, 'Estela', 2, 2),\
                    (8, 2, 'Elias', 25, 15),\
                    (9, 2, 'Designer', 3, 1),\
                    (10, 2, 'Pistela', 2, 9),\
                    (12, 3, 'Moskito', 3, 5),\
                    (13, 3, 'Kira', 1, 9),\
                    (16, 3, 'Alsaher', 7, 1),\
                    (17, 3, 'Rodrix', 2, 20),\
                    (18, 3, 'Lalitax', 7, 5);")

        #Inserindo partidas
        cur.execute("INSERT INTO `partida` (`partida_id`, `timeA_id`, `timeB_id`, `abates_timeA`, `abates_timeB`, `vencedor_id`, `torneio_id`) VALUES\
                    (1, 1, 2, 20, 10, 1, '1'),\
                    (2, 2, 3, 30, 15, 2, '1'),\
                    (3, 1, 3, 10, 5, 1, '1');")

        #Inserindo Personagens
        cur.execute("INSERT INTO `personagem` (`personagem_id`, `personagem_nome`, `personagem_preco`) VALUES\
                    (1, 'Ashe', 1200),\
                    (2, 'Vayne', 2000),\
                    (3, 'Tryndamere', 1200),\
                    (4, 'Blitzcrank', 2000),\
                    (5, 'Amumu', 2000),\
                    (6, 'Fiora', 4500),\
                    (7, 'Sona', 6300),\
                    (10, 'Alistar', 900),\
                    (8, 'Morgana', 6300),\
                    (9, 'Kayle', 4500);")

        #Inserindo Personagens_comprados
        cur.execute("INSERT INTO `personagem_comprado` (`personagem_id`, `jogador_id`) VALUES\
                    (1, 1),\
                    (2, 1),\
                    (3, 1),\
                    (4, 1),\
                    (5, 1),\
                    (1, 2),\
                    (2, 2),\
                    (1, 3),\
                    (4, 3);")

        #Inserindo Times
        cur.execute("INSERT INTO `time` (`time_id`, `nome_time`, `abates`, `mortes`) VALUES\
                    (1, 'BepidPower', 30, 15),\
                    (2, 'AlbusNox', 40, 35),\
                    (3, 'Invocados', 20, 40);")

        #Inserindo Torneio
        cur.execute("INSERT INTO `torneio` (`torneio_id`, `regiao_torneio`) VALUES\
                    (1, 'Brasil');")

     except mdb.Error as e:

        print("Error %d: %s" % (e.args[0],e.args[1]))
        sys.exit(1)

     finally:

        if con:
            con.close()

def insertRow(option: int):
    print("TODO")
    #TODO: inserção de novas linhas em cada tabela

def deleteTables():
     try:
        con = mdb.connect('localhost', 'user', 'goodPassword', 'league');

        cur = con.cursor()

        cur.execute("DROP TABLE jogador")
        cur.execute("DROP TABLE partida")
        cur.execute("DROP TABLE personagem")
        cur.execute("DROP TABLE personagem_comprado")
        cur.execute("DROP TABLE time")
        cur.execute("DROP TABLE torneio")

        cur.execute("SHOW TABLES")
        rows = cur.fetchall()

        for row in rows:
            print(row)

     except mdb.Error as e:

            print("Error %d: %s" % (e.args[0],e.args[1]))
            sys.exit(1)

     finally:

            if con:
                con.close()
