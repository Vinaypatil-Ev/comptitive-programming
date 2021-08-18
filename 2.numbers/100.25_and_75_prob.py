from math import floor
import random as r

def rand50():
    return floor(r.random()*10) & 1


def rand70():
    return rand50() | rand50()
    

if __name__ == "__main__":
    for i in range(10):
        print(rand70(), end="")