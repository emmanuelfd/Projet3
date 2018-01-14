#! /usr/bin/env python3
# coding: utf-8
from random import randint
import os
import pygame

class BoardGame:
    """in order to create the board game + loading items"""
    BOARD = []
    SIZE = 16

    def __init__(self):
        pass

    @classmethod
    def initialize_board(self, layout):
        """initializion : load the layout from file to build a 2D maze (lists in lists)
        + loading 3 items at random position + loading pictures
        """
        directory = os.path.dirname(__file__)##get the path of the this file
        #go to layout folder and select the layout set in the fct call
        path_to_file = os.path.join(directory, "layout", str(layout) + "_layout.txt")
        with open(path_to_file, 'r') as file:
            board = []
            for line in file:
                i = 0
                list_second = [] # slice line in a list
                while i < 15: #not working for class variable - to avoid newline caracter
                    list_second.append(int(line[i]))# in integer rather str for later
                    i += 1
                board.append(list_second)#add line to the global list

        i = 1
        while i < 4: #3 items to drop (4 -1)
            random_x = randint(0, 14) # random coordinate in the board
            random_y = randint(0, 14)

            random_item = board[random_x][random_y] #check the value

            if random_item == 1: # if not a wall
                board[random_x][random_y] = i + 1 # change from 1 to other int
                i += 1#incrementation - find a place for next item

            else:
                continue # it's a wall back to the while, no incrementaton another try/

        return board
    @classmethod
    def load_board(self, board, window, wall, floor, item, ether, mcgyver, wayout):
        """load pictures using pygame - board, window, wall, item, mcgyver, wayout"""
        line_x = 0#first line
        for cases in board:
            cell_y = 0#first column
            for case in cases:
                if case == 0:
                    window.blit(wall, (cell_y, line_x))
                    cell_y += 40#30 because cell is 30 px - so go to next cell

                elif case == 1:#if corridor
                    window.blit(floor, (cell_y, line_x))
                    cell_y += 40

                elif case == 2:#if items
                    window.blit(ether, (cell_y, line_x))
                    cell_y += 40

                elif case == 3 or case == 4:#if items
                    window.blit(item, (cell_y, line_x))
                    cell_y += 40

                elif case == 9:#wayout
                    window.blit(wayout, (cell_y, line_x))
                    cell_y += 40

                elif case == 5:#mcgyver
                    window.blit(mcgyver, (cell_y, line_x))
                    pygame.display.flip()
                    cell_y += 40

                else:
                    cell_y += 40
            line_x += 40#line_x is the line, so go to next line
        return(board)


class McGyver:
    """mc_gyver set with positions (0,0 to start), items and fct fight to exit
    """

    def __init__(self):
        """Mcgyver starts at 0,0 corner up and left and 0 items/goodies"""
        self.goodies = 0 # items collected
        self.position_x = 0 # starting position with board[x][y]
        self.position_y = 0
        self.new_position_x = 0 # with board[x][y]
        self.new_position_y = 0

    def fight(self):
        """to win gyvwe must have collected 3 items"""
        if self.goodies == 3:
            win = 1
        else:
            win = 0
        return win


class Position:
    """to manage mcgyver's movement"""

    def __init__(self, position_x, position_y, board):
        """position is set with x and y + a board game"""
        self.position_x = position_x #
        self.position_y = position_y
        self.board = board # board to check new position, wall, item or exit

    def new_position(self):
        """to check if a move is allowed"""
        if self.position_x < 0 or self.position_y < 0 or self.position_x > 14 or self.position_y > 14: # out the board
            move = 0#no move before cell assignation to avoid out of range error

        else:#if in the board we check if we can move
            cell = self.board[self.position_x][self.position_y]
            if cell == 0: # wall ! can't move
                move = 0#no move
            elif cell == 2 or cell == 3 or cell == 4:
                move = 2#move +you got an item?
            elif cell == 9:
                move = 3#means fight to exit
            else:
                move = 1#RAS move that's it

        return move