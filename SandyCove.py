from InnerBurialChamber import *
from RoyalTomb import *

def SandyCove(player):
    
    directions = ["FORWARD", "BACKWARD"]
    
    print("YOU ARE IN A SANDY COVE")
    
    if player["hasTorch"] == False:
        print("HINT TO TORCH")
        
    if player["hasAxe"] == False:
        print("HINT TO AXE")
        
    if player["hasTorch"] and player["hasAxe"]:
        print("TAKE ANOTHER SHOT AT THE RIDDLE")
        #UNLOCK RIDDLE SOMEHOW
    
    #Check health, refill if under full, say something if full
    
    print("YOU CAN TRAVEL FORWARD OR BACKWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    
    userInput = ''
    
    while userInput not in directions:
        print("CHOICES: FORWARD, BACKWARD")
        print("WHERE DO YOU WANT TO MOVE?")
        userInput = input().strip().upper()
        
        if userInput == "FORWARD":
            print("FORWARD: TO ROYAL TOMB")
            RoyalTomb(player)
        
        elif userInput == "BACKWARD":
            print("BACKWARD: TO INNER BURIAL CHAMBER")
            InnerBurialChamber(player)
        
        else:
            print("Please enter a valid direction.")

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
    
    SandyCove(player)