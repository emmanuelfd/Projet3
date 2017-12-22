
from random import randint
from premier import *


pitch = board_game.initialize_board()
print(pitch)
gyver = mc_gyver()
game_on = True# true means games is on

while game_on:

    action = input("L for left/R for right / U for up / D for down")

    if action.upper() == "L":
        gyver.new_position_x = gyver.position_x
        gyver.new_position_y = gyver.position_y - 1
    elif action.upper() == "R":
        gyver.new_position_x = gyver.position_x
        gyver.new_position_y = gyver.position_y + 1
    elif action.upper() == "U":
        gyver.new_position_x = gyver.position_x + 1
        gyver.new_position_y = gyver.position_x + 1
    elif action.upper() == "D":
        gyver.new_position_x = gyver.position_x - 1
        gyver.new_position_y = gyver.position_x - 1
    else:
        print("problem")
	
	# on passe posution avec les x, y et le board
    next_move = position(gyver.new_position_x,gyver.new_position_y,pitch) # not sur we need this one TBC
    next_move = position.new_position(next_move)# 
	
    if next_move == 0: # wall or out of boundary
        print("can't go that way !")
        continue
    elif next_move == 1:
        pitch[gyver.position_x][gyver.position_y] = 1#current position is set to 1 mcgyver is gone
        gyver.position_x = gyver.new_position_x#old position is now new postion
        gyver.position_y = gyver.new_position_y
        pitch[gyver.new_position_x][gyver.new_position_y] = 5#5 is mc_giver

    elif next_move == 2:
        pitch[gyver.position_x][gyver.position_y] = 1#current position is set to 1 mcgyver is gone
        gyver.position_x = gyver.new_position_x#old position is now new postion
        gyver.position_y = gyver.new_position_y
        pitch[gyver.new_position_x][gyver.new_position_y] = 5#5 is mc_giver
        gyver.goodies += 1
    elif next_move == 3:#fight and sortie
        exit = gyver.fight()
        if exit == 1:
            print("well you are out!!")
            game_on = False#breaking the while to stop the game	
        else:
            print("you lost! remember to collet the 3 items first !!")
            game_on = False #breaking the while to stop the game	
    else:
        print("problem move")#shouldn't enter here
	

    print(pitch)
	
   #affiche le board
   # fin boucle 
