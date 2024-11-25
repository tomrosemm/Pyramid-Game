#Import rooms
from Entrance import *
from Encampment import *
from SnakeWay import *
from LesserBurialChamber import *
from SphinxRoom import *
from Armory import *
from InnerBurialChamber import *
from SandyCove import *
from RoyalTomb import *
from TreasureChamber import *

#Import Systems
from Combat import *

#External Libraries to try out
import blessings
import pyfiglet
import names
import prompt_toolkit
import numpy

if __name__ == "__main__":
    
    player = {
        "name": "Player",
        "health": 100,
        "baseDamageRange": (10,20),
        "hasAxe": False,
        "hasSword": False,
        "axeBonus": (5, 10),
        "swordBonus": (10,15),
        "hasTorch": False
    }

    roomStates = {}
    
    while True:
        print("WELCOME TO THE GAME")
        
        #Allow for random name choice form names
        
        new_name = input("Enter the player's name: ").strip()
        
        if new_name:
            player["name"] = new_name
            print(f"Player's name updated to: {player['name']}")
        else:
            print("Name cannot be empty. Using default name.")
            
        Entrance(player, roomStates)
