#! /usr/bin/env python3
# coding: utf-8

import pygame
from pygame.locals import *
from random import randint
from premier import *


pitch = BoardGame.initialize_board(1)#load layout #1

gyver = McGyver()
game_on = True# true means games is on

print(pitch)

pygame.init()#pygame initialization

window = pygame.display.set_mode((450, 450))#because 450 is 30pixel per sprite
background = pygame.image.load("picture/fond.jpg").convert_alpha()#assign variable for background
square = pygame.image.load("picture/mur.png").convert_alpha()#assign variable for wall
item = pygame.image.load("picture/item.png").convert_alpha()#assign variable for items
exit = pygame.image.load("picture/exit.png").convert_alpha()##assign variable for exit picture
dk = pygame.image.load("picture/dk.png").convert_alpha()#assign variable for donkey
window.blit(background,(0,0))#load background on screen

while game_on:
	
    pygame.time.Clock().tick(30)#avoid  pitcture to blink
    window.blit(background,(0,0))#reload the background to hide old position of giver

    ##pitch = BoardGame.load_board(pitch) ## a tester 
    
##reload stuff on the board 
    x=0
    for cases in pitch:
        y=0
        for case in cases:
            if case == 0:
                window.blit(square,(y,x))
                y += 30
         
            elif case == 2 or case == 3 or case == 4:#on pose les items
                window.blit(item,(y,x))
                y += 30
                
            elif case == 9:#on pose l arrivee
                window.blit(exit,(y,x))
                y += 30

            elif case == 5:#on pose l arrivee
                window.blit(dk,(y,x))
                pygame.display.flip()
                y += 30
                
            else:
                y +=30
        x+=30

    pygame.display.flip()

## to play without graph
##    action = input("L for left/R for right / U for up / D for down")
##
##    if action.upper() == "L":
##        gyver.new_position_x = gyver.position_x
##        gyver.new_position_y = gyver.position_y - 1
##    elif action.upper() == "R":
##        gyver.new_position_x = gyver.position_x
##        gyver.new_position_y = gyver.position_y + 1
##    elif action.upper() == "U":
##        gyver.new_position_x = gyver.position_x + 1
##        gyver.new_position_y = gyver.position_y
##    elif action.upper() == "D":
##        gyver.new_position_x = gyver.position_x - 1
##        gyver.new_position_y = gyver.position_y
##    else:
##        print("problem, you should enter L for left/R for right / U for up / D for down")	

#now with Pygame
    for event in pygame.event.get():##wait for keyboard events to move gyver position
        if event.type == KEYDOWN and event.key == K_LEFT:
            gyver.new_position_x = gyver.position_x
            gyver.new_position_y = gyver.position_y - 1
            
        if event.type == KEYDOWN and event.key == K_RIGHT:
            gyver.new_position_x = gyver.position_x
            gyver.new_position_y = gyver.position_y + 1

        if event.type == KEYDOWN and event.key == K_DOWN:
            gyver.new_position_x = gyver.position_x + 1
            gyver.new_position_y = gyver.position_y

        if event.type == KEYDOWN and event.key == K_UP:
            gyver.new_position_x = gyver.position_x - 1
            gyver.new_position_y = gyver.position_y
	
    print(gyver.new_position_x)
    print(gyver.new_position_y)
    #on passe posution avec les x, y et le board
    next_move = Position(gyver.new_position_x,gyver.new_position_y,pitch) # not sur we need this one TBC

    next_move = Position.new_position(next_move)#
    #print(str(next_move) + "ttttr")
	
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
        print("nice you have just collected a new goodies")
        print("you need " + str((3 - gyver.goodies)) + " more iterms to walk out !!")
    elif next_move == 3:#fight and sortie
        exit = gyver.fight()
        if exit == 1:
            print("well you are out!!")
            game_on = False#breaking the while to stop the game	
        else:
            print("you lost! remember to cocllet  3 items first !!")
            game_on = False #breaking the while to stop the game	
    else:
        print("problem move")#shouldn't enter here
	

    print(pitch)
	
   #affiche le board
   # fin boucle 
