from Domains import Circle, Player, AI, Board

class UI:

    @staticmethod
    def PrintMenu():
        string = "Available game modes: \n"
        string += "1. Human vs Human \n"
        string += "2. Human vs Computer \n"
        string += "0. Exit"
        print(string)

    @staticmethod
    def ValidCommands(command):
        availableCommands = ['1', '2', '0']
        return command in availableCommands

    @staticmethod
    def checkColumnInteger(msg):

        if msg.isdigit():
            column = int(msg)
            if column > 0 and column < 8:
                return True
        return False

    def Human_VS_Computer(self):

        C1 = Circle('yellow')
        C2 = Circle('magenta')
        name = input("Please type your name: ")
        Player1 = Player(name, C1)
        Player2 = AI(C2, C1, 4)
        B = Board()
        print(Player1)
        print(Player2)
        print(B)

        while(B.isDraw() == False):
            col1 = input(Player1.getname() + ", choose your column: ")
            while (self.checkColumnInteger(col1) == False):
                col1 = input("Please choose a number between 1 and 7: ")
            col1 = int(col1)
            col1 -= 1
            while B.move(Player1.getcircle(), col1) == False:
                col1 = input("Please choose a column which is not full: ")
                while (self.checkColumnInteger(col1) == False):
                    col1 = input("Please choose a number between 1 and 7: ")
                col1 = int(col1)
                col1 -= 1
            print(B)
            if B.isGameWon() == True:
                print(Player1.getname() + " wins.")
                break
            print("The computer is thinking... ")
            col2 = int(Player2.move(B))
            print("The computer chose column: " + str(col2 + 1))
            B.move(Player2.getcircle(), col2)
            print(B)
            if B.isGameWon() == True:
                print("The computer wins.")
                break

        if B.isDraw() == True:
            print("Draw")

        print("\n")
        print("\n")

    def Human_VS_Human(self):

        C1 = Circle('yellow')
        C2 = Circle('magenta')
        name1 = input("Player 1, please type your name: ")
        Player1 = Player(name1, C1)
        name2 = input("Player 2, please type your name: ")
        Player2 = Player(name2, C2)
        B = Board()
        print(Player1)
        print(Player2)
        print(B)

        while (B.isDraw() == False):
            col1 = input(Player1.getname() + ", choose your column: ")
            while (self.checkColumnInteger(col1) == False):
                col1 = input("Please choose a number between 1 and 7: ")
            col1 = int(col1)
            col1 -= 1
            while B.move(Player1.getcircle(), col1) == False:
                col1 = input("Please choose a column which is not full: ")
                while (self.checkColumnInteger(col1) == False):
                    col1 = input("Please choose a number between 1 and 7: ")
                col1 = int(col1)
                col1 -=1
            print(B)
            if B.isGameWon() == True:
                print(Player1.getname() + " wins.")
                break
            col2 = input(Player2.getname() + ", choose your column: ")
            while (self.checkColumnInteger(col2) == False):
                col2 = input("Please choose a number between 1 and 7: ")
            col2 = int(col2)
            col2 -= 1
            while B.move(Player2.getcircle(), col2) == False:
                col2 = input("Please choose a column which is not full: ")
                while (self.checkColumnInteger(col2) == False):
                    col2 = input("Please choose a number between 1 and 7: ")
                col2 = int(col2)
                col2 -= 1
            print(B)
            if B.isGameWon() == True:
                print(Player2.getname() + " wins.")
                break

        if B.isDraw() == True:
            print("Draw")

        print("\n")
        print("\n")

    def MainMenu(self):

        commandDict = {'1': self.Human_VS_Human,
                       '2': self.Human_VS_Computer}

        while True:
            UI.PrintMenu()
            command = input("Please choose your command: ")
            while not UI.ValidCommands(command):
                command = input("Please type a valid command!")
            if command == '0':
                break
            commandDict[command]()

Game = UI()
Game.MainMenu()


