from termcolor import colored
import unittest

class Circle:

    def __init__(self, color):
        """
        initializer for the Circle class
        Input: color of the circle
        """
        self.color = color

    def __str__(self):
        """
        Returns a circle of the color specified
        """
        return colored('●', str(self.color))


class Board:

    def __init__(self):
        """
        Initializer for the Board class
        It contains a pseudo-matrix which memories the state of the board
        """
        self.matrix = [['●' for x in range(7)] for y in range(6)]

    def __str__(self):
        """
        Returns the configuration of the board as a string/board
        """
        string = '------------------\n'
        for i in range(6):
            for j in range(7):
                string += '|'
                string += str(self.matrix[i][j])
            string += '|\n'
            string += '------------------\n'
        return string

    def isGameWon(self):
        """
        checks if the game was won be someone or the computer
        Returns True if the game was won, False otherwise
        """

        for i in range(6):
            for j in range(4):
                if self.matrix[i][j] != '●':
                    if self.matrix[i][j] == self.matrix[i][j + 1]:
                        if self.matrix[i][j] == self.matrix[i][j + 2]:
                            if self.matrix[i][j] == self.matrix[i][j + 3]:
                                return True

        for i in range(7):
            for j in range(3):
                if self.matrix[j][i] != '●':
                    if self.matrix[j][i] == self.matrix[j + 1][i]:
                        if self.matrix[j][i] == self.matrix[j + 2][i]:
                            if self.matrix[j][i] == self.matrix[j + 3][i]:
                                return True

        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] != '●':
                    if self.matrix[i][j] == self.matrix[i + 1][j + 1]:
                        if self.matrix[i][j] == self.matrix[i + 2][j + 2]:
                            if self.matrix[i][j] == self.matrix[i + 3][j + 3]:
                                return True

        for i in range(3):
            j = 6
            while j > 2:
                if self.matrix[i][j] != '●':
                    if self.matrix[i][j] == self.matrix[i + 1][j - 1]:
                        if self.matrix[i][j] == self.matrix[i + 2][j - 2]:
                            if self.matrix[i][j] == self.matrix[i + 3][j - 3]:
                                return True
                j -= 1

        return False

    def isDraw(self):
        """
        checks if the game is a draw
        Returns True if the game is a draw and False otherwise
        """
        for i in range(6):
            for j in range(7):
                if self.matrix[i][j] == '●':
                    return False

        return True

    def move(self, circle, column):
        """
        method that enables a move on the board
        Input: the colour of the circle and the column in which the column will be introduced
        Returns True if the move is possible on that column, false otherwise
        """
        i = 5
        while i > -1:
            if self.matrix[i][column] == '●':
                self.matrix[i][column] = circle
                return True
            i -= 1
        return False


class Player:

    def __init__(self, name, circle):
        """
        Initializer for the Player Class
        Input: name of the player
               the circle which the player will use
        """
        self.name = name
        self.circle = circle

    def getcircle(self):
        """
        getter for the circle attribute
        """
        return self.circle

    def getname(self):
        """
        getter for the name attribute
        """
        return self.name

    def __str__(self):
        return self.name + " is playing with circles of this color: " + str(self.circle)

class AI:

    def __init__(self, circle, oppcircle, difficulty):
        """
        initializer for the AI class
        Input: circle: the circle to be used by the computer
               oppcircle: the circle used by the opponent
               difficulty: the depth at which the computer will look further for its moves
        """
        self.circle = circle
        self.difficulty = difficulty
        self.oppcircle = oppcircle

    def getcircle(self):
        """
        getter for circle attribute
        """
        return self.circle

    def __str__(self):
        return "The computer is playing with circles of this color: " + str(self.circle)

    def islegalmove(self, board, column):
        """
        checks if the move is legal for a given state of a board and a column
        Input: board
               column
        Returns True if the move is legal, False otherwise
        """
        i = 5
        while i > -1:
            if board.matrix[i][column] == '●':
                return True
            i -= 1
        return False

    def simulatemove(self, board, column, circle):
        """
        simulates a move for the minimax algorithm
        Input: board - the state of the board before the simulated move
               column - the column in which the move will be made
               circle - the circle to be introduced in the board
        Returns a virtual board in which the move was made
        """
        board2 = Board()
        for i in range(6):
            for j in range(7):
                board2.matrix[i][j] = board.matrix[i][j]
        board2.move(circle, column)
        return board2

    def move(self, board):
        """
        searches for the best move for a given state of the board
        Input: the state of the board
        Returns the best move as a column number
        """
        legalmoves = {}
        for i in range(7):
            if self.islegalmove(board, i):
                board2 = self.simulatemove(board, i, self.circle)
                legalmoves[i] = -self.find(self.difficulty - 1, board2, self.oppcircle)

        bestscore = -99999999
        bestmove = None
        moves = legalmoves.items()
        for move,score in moves:
            if score > bestscore:
                bestscore = score
                bestmove = move

        return bestmove

    def find(self, depth, board, circle):
        """
        finds the score of a move by recursively completing a virtual board until the depth parameter reaches 0
        Input depth: the "depth" at which the board will be populated with moves
              board: the state of the board to find the score of a certain move
              circle: the circle of the certain move
        Returns the score of the move calculated using an heuristic
        """
        legalmoves = []
        for i in range(7):
            if self.islegalmove(board, i):
                board2 = self.simulatemove(board, i, circle)
                legalmoves.append(board2)

        if depth == 0 or len(legalmoves) == 0 or board.isGameWon():
            return self.value(board, circle)

        if circle == self.circle:
            oppcircle = self.oppcircle
        else:
            oppcircle = self.circle

        score = -99999999
        for i in legalmoves:
            score = max(score, -self.find(depth - 1, i, oppcircle))
        return score

    def value(self, board, circle):
        """
        calculates the value for a configuration of the table using a certain heuristic
        Input board:
              circle:
        Returns the score of a configuration of the table
        """
        if circle == self.circle:
            oppcircle = self.oppcircle
        else:
            oppcircle = self.circle

        mfours = self.checkForConnection(board, circle, 4)
        mthrees = self.checkForConnection(board, circle, 3)
        mtwos = self.checkForConnection(board, circle, 2)
        ofours = self.checkForConnection(board, oppcircle, 4)
        othrees = self.checkForConnection(board, oppcircle, 3)
        otwos = self.checkForConnection(board, oppcircle, 2)
        if ofours > 0:
            return -100000
        else:
            return mfours*100000 + mthrees*100 + mtwos - othrees*100 - otwos

    def checkForConnection(self, board, circle, length):
        """
        calculates the number of connections of certain length for a configuration of the board for a certain player
        Input board: the configuration of the table
              circle: the circle of the player
              length: the length of the connections to be looked for
        Returns the number of connections
        """
        count = 0
        for i in range(6):
            for j in range(7):
                if board.matrix[i][j] == circle:
                    count += self.findVerConnection(i, j, board, length, board.matrix[i][j])
                    count += self.findHorConnection(i, j, board, length, board.matrix[i][j])
                    count += self.findDiaConnection(i, j, board, length, board.matrix[i][j])
        return count

    def findVerConnection(self, i, j, board, length, circle):
        """
        calculates the number of vertical connections for a certain position
        Input i: the height of the position
              j: the width of the position
              board: the state of the board
              length: the length of the connections needed
              circle: the connections which are looked for need to be of this circle
        Returns the number of the connections found with all the characteristics mentioned
        """
        count = 0
        if i + length - 1 < 6:
            for x in range(length):
                if board.matrix[i + x][j] == circle:
                    count += 1
                else:
                    break

        if count == length:
            return 1
        else:
            return 0

    def findHorConnection(self, i, j, board, length, circle):
        """
        calculates the number of horizontal connections for a certain position
        Input i: the height of the position
              j: the width of the position
              board: the state of the board
              length: the length of the connections needed
              circle: the connections which are looked for need to be of this circle
        Returns the number of the connections found with all the characteristics mentioned
        """
        count = 0
        if j + length - 1 < 7:
            for x in range(length):
                if circle == board.matrix[i][j + x]:
                    count += 1
                else:
                    x = length + 1
        if count == length:
            return 1
        else:
            return 0

    def findDiaConnection(self, i, j, board, length, circle):
        """
        calculates the number of diagonal connections for a certain position
        Input i: the height of the position
              j: the width of the position
              board: the state of the board
              length: the length of the connections needed
              circle: the connections which are looked for need to be of this circle
        Returns the number of the connections found with all the characteristics mentioned
        """
        total = 0
        count = 0
        if j + length - 1 < 7 and i + length - 1 < 6:
            for x in range(length):
                if circle == board.matrix[i + x][j + x]:
                    count += 1
                else:
                    x = length + 1
        if count == length:
            total += 1

        count = 0
        if j + length - 1 < 7 and i - length + 1 > -1:
            for x in range(length):
                if circle == board.matrix[i - x][j + x]:
                    count += 1
                else:
                    x = length + 1
        if count == length:
            total += 1

        return total


class Tests(unittest.TestCase):

    def testboard(self):
        C1 = Circle('yellow')
        C2 = Circle('magenta')
        B = Board()
        B.matrix[5][0] = C1
        B.matrix[4][1] = C1
        B.matrix[3][2] = C1
        B.matrix[5][1] = C2
        B.matrix[5][2] = C2
        B.matrix[4][2] = C2
        B.matrix[2][2] = C2
        B.matrix[1][2] = C1
        B.matrix[0][2] = C2
        assert B.move(C1, 2) == False
        assert B.move(C1, 0) == True
        assert B.matrix[4][0] == C1
        assert B.isGameWon() == False
        assert B.isDraw() == False
        B.move(C1, 0)
        B.move(C1, 0)
        assert B.isGameWon() == True

    def testplayer(self):
        C1 = Circle('yellow')
        C2 = Circle('magenta')
        P1 = Player("Mio Naruse", C1)
        P2 = Player("Al Bundy", C2)
        assert P1.getname() == "Mio Naruse"
        assert P2.getcircle() == C2

    def testAI(self):
        C1 = Circle('yellow')
        C2 = Circle('magenta')
        P1 = Player("Mio Naruse", C1)
        P2 = AI(C2, P1.getcircle(), 2)
        B = Board()
        B.matrix[5][0] = C1
        B.matrix[4][1] = C1
        B.matrix[3][2] = C1
        B.matrix[5][1] = C2
        B.matrix[5][2] = C2
        B.matrix[4][2] = C2
        B.matrix[2][2] = C2
        B.matrix[1][2] = C1
        B.matrix[0][2] = C2
        assert P2.getcircle() == C2
        assert P2.islegalmove(B, 2) == False
        assert P2.islegalmove(B, 1) == True
        B2 = P2.simulatemove(B, 1, P2.getcircle())
        assert B2.matrix[3][1] == C2
        assert P2.findVerConnection(4, 2, B, 2, C2) == 1
        assert P2.findVerConnection(4, 2, B, 3, C2) == 0
        assert P2.findVerConnection(5, 2, B, 2, C2) == 0
        assert P2.findHorConnection(5, 1, B, 2, C2) == 1
        assert P2.findHorConnection(5, 2, B, 2, C2) == 0
        assert P2.findHorConnection(5, 1, B, 4, C2) == 0
        assert P2.findDiaConnection(5, 0, B, 3, C1) == 1
        assert P2.findDiaConnection(5, 0, B, 4, C1) == 0
        assert P2.findDiaConnection(4, 1, B, 3, C1) == 0
        assert P2.findDiaConnection(5, 0, B, 2, C1) == 1
        B.move(C2, 3)
        assert P2.findDiaConnection(4, 2, B, 2, C2) == 1
        assert P2.findDiaConnection(5, 3, B, 2, C2) == 0
        assert P2.findDiaConnection(4, 2, B, 3, C2) == 0
        assert P2.checkForConnection(B, C1, 2) == 2
        assert P2.checkForConnection(B, C2, 3) == 1
        assert P2.checkForConnection(B, C1, 4) == 0
        assert P2.checkForConnection(B, C1, 3) == 1
        assert P2.checkForConnection(B, C2, 2) == 5
        assert P2.checkForConnection(B, C2, 4) == 0
        assert P2.value(B, C2) == 3
        assert P2.value(B, C1) == -3
        assert P2.find(2, B, C1) == -105
        assert P2.find(2, B, C2) == 100000
        assert P2.move(B) == 4


# Player2 = AI(C1, C2, 2)
# Player1 = Player("Alexia", C2)
# B = Board()
# print(Player1)
# print(Player2)
# B.matrix[5][0] = C1
# B.matrix[4][1] = C1
# B.matrix[3][2] = C1
# B.matrix[5][1] = C2
# B.matrix[5][2] = C2
# B.matrix[4][2] = C2
# B.matrix[2][2] = C2
# B.matrix[1][2] = C1
# B.matrix[0][2] = C2
# B.move(C2, 3)
# print(B)
# print(Player2.find(2,B,C2))
# print(Player2.find(2,B,C1))
# print(Player2.move(B))

if __name__ == '__main__':
    unittest.main()
# while(B.isDraw() == False):
#     col1 = int(input(Player1.getname() + ", choose your column: "))
#     col1 -= 1
#     B.move(Player1.getcircle(), col1)
#     print(B)
#     if B.isGameWon() == True:
#         print(Player1.getname() + " wins")
#         break
#     print("Computer is moving: ")
#     col2 = int(Player2.move(B))
#     B.move(Player2.getcircle(), col2)
#     print(B)
#     if B.isGameWon() == True:
#         print("Computer wins")
#         break


# B.matrix[0][3] = C1
# B.matrix[5][3] = C1
# B.matrix[4][3] = C1
# B.matrix[1][3] = C1
# B.matrix[2][3] = C1
# B.matrix[3][4] = C1
# B.matrix[4][5] = C1
# B.matrix[5][6] = C2
# B.matrix[3][0] = C1
# B.matrix[2][5] = C1
# B.matrix[3][4] = C1
# B.matrix[3][3] = C2
# P1 = Player(1, C1)
# print(B.move(C1, 3))
# print(B)
# print(B.isGameWon())
# print(B.isDraw())
# print(P1)
