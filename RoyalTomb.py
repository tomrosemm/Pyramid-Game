from TreasureChamber import *

from Combat import *

def RoyalTomb(player, roomStates):
    
    #Setup some way to save that combat in this room has already happened, check against it before running combat
    
    directions = ["LEFT", "BACKWARD", "Q"]    
    
    print("YOU ARE IN THE ROYAL TOMB")
    
    print("YOU ARE ATTACKED BY 3 TOMB GOBLINS AND 2 MUMMIES")
        
    if player["hasAxe"] and not player["hasSword"]:
        print("YOU HAVE AN AXE")
    
    elif player["hasSword"]:
        print("YOU HAVE A HOOKED SWORD")
    
    else:
        print("STRAP IN")
    
    print("BEGIN BATTLE")
    
    #Call combat, return bool for won
    combatWon = True
    
    print("TIME TO BATTLE!")
    print("LET'S SAY YOU WON FOR NOW")
    
    print("YOU CAN TRAVEL FORWARD OR BACKWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
    
    while userInput not in directions:        
        print("CHOICE(S): LEFT, BACKWARD")
        print("Q TO QUIT")
        userInput = input().strip().upper()

        if userInput == "LEFT":   
            print("FORWARD: TO TREASURE CHAMBER") #Test Print
            TreasureChamber(player, roomStates)
        
        elif userInput == "BACKWARD":
            from SandyCove import SandyCove
            print("BACKWARD: TO SANDY COVE")
            SandyCove(player, roomStates)
            
        elif userInput == "Q":
            print("GOODBYE")
            quit()
            
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
    
    roomStates = {}
    
    RoyalTomb(player, roomStates)