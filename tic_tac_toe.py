#Player
class Player():
    winnner = False

    def __init__(self,name, shape):
        self.name = name
        self.shape = shape

#Game board
class Game_board():
    def __init__(self):
        self.game_board =["-","-","-","-","-","-","-","-","-"]

#Display board
    def print_board(self):
        print("     |{A1}|{A2}|{A3}|".format(A1=self.game_board[0], A2=self.game_board[1], A3=self.game_board[2]))
        print("     |{B1}|{B2}|{B3}|".format(B1=self.game_board[3], B2=self.game_board[4], B3=self.game_board[5]))
        print("     |{C1}|{C2}|{C3}|".format(C1=self.game_board[6], C2=self.game_board[7], C3=self.game_board[8]))
        print("")

#Check if Position is filled
    def position_filled(self, position):
        index = position - 1
        if str(self.game_board[index]) == "X" or str(self.game_board[index]) == "O":
            return True
        else:
            return False

#Check Win
    def check_win(self,shape):
        #Create list of positions owned
        own_index=[]
        for index in range(len(self.game_board)):
            if self.game_board[index] == str(shape):
                own_index.append(int(index))

        #Checks thru list
        if 0 in own_index and 1 in own_index and 2 in own_index:
            return True
        elif 3 in own_index and 4 in own_index and 5 in own_index:
            return True
        elif 6 in own_index and 7 in own_index and 8 in own_index:
            return True
        elif 0 in own_index and 3 in own_index and 6 in own_index:
            return True
        elif 1 in own_index and 4 in own_index and 7 in own_index:
            return True
        elif 2 in own_index and 5 in own_index and 8 in own_index:
            return True
        elif 0 in own_index and 4 in own_index and 8 in own_index:
            return True
        elif 2 in own_index and 4 in own_index and 6 in own_index:
            return True
        else:
            return False

#Add Shape
    def add_shape(self,shape):
        position = int(input("Where would you like to go? \n"))
        while self.position_filled(position) == True:
            position = int(input("Spot taken try again! \n"))
        self.game_board[position-1] = shape

        


#--------Runtime-------------------------------
print("\nWelcome to Tic Tac Toe!")
print("=======================")

game = Game_board()

player1_name = input("What is your name? \n")
player1 = Player(player1_name, "X")

player2_name = input("What is your opponenet's name? \n")
player2 = Player(player2_name, "O")

while True:
    game.print_board()
    game.add_shape(player1.shape)
    if game.check_win(player1.shape) == True:
        print("===================")
        print(str(player1.name) + " wins")
        break
    else:
        game.print_board()
        game.add_shape(player2.shape)
        if game.check_win(player2.shape) == True:
            print("===================")
            print(str(player2.name) + " wins")
            break

game.print_board()
print("GG")





