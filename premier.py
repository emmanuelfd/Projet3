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

            random_item = board[random_x][random_y] # check the value 
			
            if random_item ==1: # if not a wall
                board[random_x][random_y] = i + 1 # change from 1 to other int 
                i += 1#incrementation - new find a place for new item
			
            else:
                continue # it's a wall back to the while, no incrementaton another try/
                
				
		
        return board
			
			
print(board_game.initialize_board())
