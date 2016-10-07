import CRUD

CRUD.deleteTables()
CRUD.createDB()
CRUD.insertRows()

option = 0

print("\nOlá! Bem-vindo ao Banco de Dados do nosso Campeonato de League Of Legends!")

while option != 3:

    print("\nMenu: \n"
          "1. Inserir Novos Dados\n"
          "2. Fazer Consultas\n"
          "3. Sair")

    option = int(input())

    if option == 1:

        print("Inserir: \n")
        print("0. Novo Jogador\n"
              "1. Nova Partida\n"
              "2. Novo Personagem\n"
              "3. Novo Personagem comprado\n"
              "4. Novo Time\n"
              "5. Novo Torneio\n"
              "6. Sair")
        writeOpt = int(input())

        #TODO: view da inserção
        if writeOpt is 0:
            CRUD.insertRow(0)
        # elif writeOpt == 1:
        #
        # elif writeOpt == 2:
        #
        # elif writeOpt == 3:
        #
        # elif writeOpt == 4:
        #
        # elif writeOpt == 5:

        elif writeOpt == 6:
            quit()


    elif option == 2:

        print("Consultas: \n"
          "0. View - Qual o time vencedor no momento?\n"
          "1. Qual o personagem mais comprado do jogo?\n"
          "2. Quais os personagens o jogador de id 1 possui?\n"
          "3. Qual jogador possui mais personagens?\n"
          "4. Mostre o jogador com mais abates de cada time\n"
          "5. Mostre todos os jogadores, seus abates e mortes do time de nome BepidPower\n"
          "6. Sair")
        readOpt = int(input())

        if readOpt is 0:
            CRUD.readTables(0)
        elif readOpt == 1:
            CRUD.readTables(1)
        elif readOpt == 2:
            CRUD.readTables(2)
        elif readOpt == 3:
            CRUD.readTables(3)
        elif readOpt == 4:
            CRUD.readTables(4)
        elif readOpt == 5:
            CRUD.readTables(5)
        elif readOpt == 6:
            quit()

    elif option == 3:
         quit()


