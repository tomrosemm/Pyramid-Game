#Import rooms
from Entrance import *
#Encampment
from SnakeWay import *
from SphinxRoom import *
#Armory
from InnerBurialChamber import *
from SandyCove import *
#Royal Tomb
#Treasure Chamber

#Import Systems
from Combat import *

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

    tombGoblin = {
        "name": "Goblin Fred",
        "health": 75,
        "damageRange": (5,15)
    }
    
    while True:
        print("WELCOME TO THE GAME")
        
        new_name = input("Enter the player's name: ").strip()
        
        if new_name:
            player["name"] = new_name
            print(f"Player's name updated to: {player['name']}")
        else:
            print("Name cannot be empty. Using default name.")
            
        Entrance(player)
