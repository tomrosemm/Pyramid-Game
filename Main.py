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
# import blessings

# import names
# import prompt_toolkit
# import numpy

def titleScreen():
    """!
    
    """
    
    try:
        import pyfiglet
        pyFigletImported = True
    except (ImportError):
        pyFigletImported = False

    if pyFigletImported:
        title = pyfiglet.figlet_format("The Pyramid", font = "5lineoblique")
        print(title)
        print()
    
    else:
        print()
        print("Welcome to Pyramid.")
        print()
        print()

if __name__ == "__main__":
    """!
    
    """
    
    player = {
        "name": "TestPlayer",
        "maxHealth": 100,
        "health": 100,
        "baseDamageRange": (10,20),
        "originalBaseDamageRange": (10,20),
        "hasAxe": False,
        "hasSword": False,
        "axeBonus": (5, 10),
        "swordBonus": (10,15),
        "hasTorch": False
    }

    roomStates = {}
    
    while True:
        titleScreen()
        
        #Allow for random name choice from names?
        
        newName = input("Enter the player's name: ").strip()
        print()
        
        if newName:
            player["name"] = newName
            print(f"Player's name updated to: {player['name']}")
            print("__________________________________________________")
            print()
            
        else:
            print("Name cannot be empty. Using default name.")
            print()
            print(f"Player's name defaults to: {player['name']}")
            print("__________________________________________________")
            print()
            
        Entrance(player, roomStates)
