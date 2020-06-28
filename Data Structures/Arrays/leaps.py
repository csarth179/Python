#!/usr/local/bin/python3                                                                                                                               

"""
Author: Sarthak Chopra
File Name: leaps.py
Date: Sun Jun 20 2020
"""

import sys
import webbrowser

print("""Game Rules:
1) Do not step out of bounds.
2) Do not land on a number which equals zero.
3) Do not step on a repeated number.
4) Do not enter a negative number.\n
For more information about this game, check out the link opened on your web browser after running this code.""")
webbrowser.open("https://stackoverflow.com/questions/55047260/recursive-one-dimensional-game-leap-current-index-n-times-repeatedly-to-the-r#_=_")

print('\nNow to begin the game, please enter a list of numbers: ')
game_board = input().split()
try:
        for index in range(len(game_board)):
                game_board[index] = int(game_board[index])
except ValueError:
        print ('Error: Invalid list of numbers!')
        sys.exit(1)

previous_index = 0
current_index = previous_index
start_position = game_board[0]
end_position = len(game_board)-1
current_element = game_board[current_index]
repeated_index = list()
current_new_index = 0

def move_right():
        global current_index
        global current_element
        global previous_index
        global repeated_index
        repeated_index.append(current_index)
        current_element = game_board[current_index]
        right_sum = 0
        # shift by sum
        for right_sum in range(0, current_element):
                right_sum += 1
        previous_index = right_sum
        current_index += right_sum
        right_sum = 0
        if(current_element == 0):
                return False
        for repeat in repeated_index:
                if(repeat == current_index):
                        return False
        if(current_index <= end_position):
                print(current_index, end = ' ')
                return True
        else:
                return False

def move_left():
        global current_index
        global current_element
        global repeated_index
        global previous_index
        global current_new_index
        current_new_index = current_index - previous_index
        current_element = game_board[current_new_index]
        left_sum = 0

        for left_sum in range(0, current_element):
                left_sum += 1
        previous_index = current_new_index
        current_new_index -= left_sum
        left_sum = 0
        if(current_element == 0):
                return False
        for repeat in repeated_index:
                if(repeat == current_new_index):
                        return False
        if(current_new_index < 0):
                return False
        if(previous_index >= start_position):
                print(current_new_index, end = ' ')
                current_index = current_new_index
                return True
        else:
                return False

def can_win():
        once = True
        # check end conditions
        if(current_element <= 0 or current_index > end_position or current_index < 0):     
                print('\nNo more actions possible! You lost!')
                sys.exit(0)
        if(current_index == end_position):
                print('\nLanded on the last number! You won!')
                sys.exit(0)
        # recursive call
        if(move_right() or move_left() or once == True):
                can_win()
                once = False

if(current_element <= 0):
        print('You lost!')
        sys.exit(0)
# print indices
if(game_board):
        print('List of possible positions to land on:', current_index, end = ' ')
        can_win()