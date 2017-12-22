from random import randint

class board_game:
    BOARD = []
    SIZE = 16

	
    def __init__(self):
        pass
    
    @classmethod		
    def initialize_board(self):
        with open('FichierDeTest.txt','r') as f:
            board = []
            for line in f:
                i=0
                e=[] # slice line in a list
                while i < 15: #not working for class variable - to avoid newline caracter
                    e.append(int(line[i]))# in integer rather str for later
                    i += 1
                board.append(e)#add  line to the global list

       
			
        i=1
        while i < 4: #3 items to drop (4 -1)
            random_x = randint(0,14) # random coordinate in the board
            random_y = randint(0,14)

            random_item = board[random_x][random_y] #check the value 
			
            if random_item ==1: # if not a wall
                board[random_x][random_y] = i + 1 # change from 1 to other int 
                i += 1#incrementation - new find a place for new item
			
            else:
                continue # it's a wall back to the while, no incrementaton another try/

        return board
		

class mc_gyver:

    def __init__(self):
        """Mcgyver get - number of object son"""
        self.goodies = 0 # items collected
        self.position_x = 0 # with board[x][y]
        self.position_y = 0
        self.new_position_x = 0 # with board[x][y]
        self.new_position_y = 0

    def fight(self):
        if self.goodies == 3:
            win = 1
        else:
            win = 0
        return win			

class position:

    def __init__(self,position_x,position_y,board):
        """Mcgyver get - number of object son"""
        self.position_x = position_x # 
        self.position_y = position_y
        self.board = board # board to check new position, wall, item or exit

    def new_position (self):
        """method to compute new positin for McGyver"""

        cell = self.board[self.position_x][self.position_y]
        if self.position_x < 0 or self.position_y < 0: # we go out the board game
            move = 0#no move
        if cell == 0: # wall ! can't move
            move = 0#no move     
        elif cell == 2 or cell == 3 or cell == 4:
            move = 2#move +you got an item?
        elif cell == 9:
            move == 3#means fight to exit
        else:
            move = 1#RAS move that's it		

        return move
		
	

