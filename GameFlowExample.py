# import Scenes/Rooms from Scenes.py
from Scenes import *

weapon = False

if __name__ == '__main__':
    while True:
        print("Welcome to the Game")
        print("Enter Name: ")
        name = input()
        print("Greetings, " + name + ", welcome to the game.")
        introScene()
