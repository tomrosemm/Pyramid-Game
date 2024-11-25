from SphinxRoom import *
from SandyCove import *

from Combat import *
    
def InnerBurialChamber(player):
    
    directions = ["RIGHT", "BACKWARD"]
    
    print("YOU ARE IN THE INNER BURIAL CHAMBER")
    
    print("YOU ARE ATTACKED BY 2 TOMB GOBLINS AND A MUMMY")
        
    if player["hasAxe"]:
        print("YOU HAVE AN AXE")
    
    else:
        print("STRAP IN")
    
    print("BEGIN BATTLE")
    
    #Call combat, return bool for won
    combatWon = True
    
    if combatWon:
        print("SUCCESSFUL BATTLE")
        print("YOU CAN TRAVEL RIGHT OR BACKWARD")
        print("WHERE DO YOU WANT TO MOVE?")
        userInput = ''
        
        while userInput not in directions:
            print("CHOICES: RIGHT, BACKWARD")
            userInput = input().strip().upper()
            
            if userInput == "RIGHT":
                print("RIGHT: TO SANDY COVE")#Test print
                SandyCove(player)
            
            elif userInput == "BACKWARD":
                print("BACKWARD: TO SPHINX ROOM")
                SphinxRoom(player)

            else:
                print("Please enter a valid direction.")

    else:
        print("YOU DIED!")
        quit()

if __name__ == '__main__':
    
    player = {
        "name": "TestPlayer",
        "health": 100,
        "baseDamageRange": (10,20),
        "hasAxe": False,
        "hasSword": False,
        "axeBonus": (5, 10),
        "swordBonus": (10,15),
        "hasTorch": False
    }
    
    InnerBurialChamber(player)