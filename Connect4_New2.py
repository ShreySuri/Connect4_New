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


list_1 = []
for i in range (0, 42):
    if i < 10:
        i = str("0%s" % i)
    list_1.append(i)

board(list_1)

