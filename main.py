import CRUD

option = 0

print("\nOlá! Bem-vindo ao Banco de Dados do nosso Campeonato de League Of Legends!\n"
      "Equipe: Gabriela, Italus, Tiago Alexandre")

while option != 6:
    print("\n---------------------------")
    print("Menu: \n"
          "0. Ver Banco de Dados\n"
          "1. Criar Tabelas\n"
          "2. Popular Tabelas\n"
          "3. Cadastrar novo Jogador\n"
          "4. Fazer Consultas\n"
          "5. Deletar todas as tabelas\n"
          "6. Sair")
    print("---------------------------")

    option = int(input())

    if option == 0:

        CRUD.readAll()

    elif option == 1:

        CRUD.createDB()

    elif option == 2:

        CRUD.insertRows()

    elif option == 3:

        CRUD.insertRow(0)

    elif option == 4:

        print("\nConsultas: \n"
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

    elif option == 5:
         CRUD.deleteTables()

    elif option == 6:
        quit()


