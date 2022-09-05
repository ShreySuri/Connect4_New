import math
import random
import time

def board(list_42):
    for i in range (0, 6):
        string = "|"
        for j in range (0, 7):
            string = "%s %s" % (string, list_42[7 * i + j])
        string = "%s|" % string
        print(string)


def game_format(list_42, input_1, symbol):
    list_42.reverse()
    input_1 = 8 - input_1
    list_val = list_42[input_1]
    current_pos = input_1
    count = 0
    while list_val != " " or count > 6:
        current_pos = current_pos + 7
        list_val = list_42[current_pos]
        count = count + 1

    if list_val == " ":
        list_42[current_pos] = symbol
        return list_42
    else:
        return False
        
list_42 = []
for i in range (0, 42):
    list_42.append(" ")

list_42 = game_format(list_42, 5, "x")

board(list_42)
