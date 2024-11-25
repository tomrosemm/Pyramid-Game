from TreasureChamber import *

from Combat import *

def RoyalTomb(player, roomStates):

    directions = ["LEFT", "BACKWARD", "Q"]    
    
    #Initialize the room states if not already done
    if "RoyalTomb" not in roomStates:
        roomStates["RoyalTomb"] = {"visited": False, "battleWon": False}
        
    if not roomStates["RoyalTomb"]["visited"]:
        print("WELCOME TO THE ROYAL TOMB FOR THE FIRST TIME")
        roomStates["RoyalTomb"]["visited"] = True
    
    else:
        print("WELCOME BACK TO THE ROYAL TOMB")
    
    print("YOU ARE IN THE ROYAL TOMB")
    
    if not roomStates["RoyalTomb"]["battleWon"]:
        print("YOU ARE ATTACKED BY 3 TOMB GOBLINS AND 2 MUMMIES")
        
        if player["hasAxe"] and not player["hasSword"]:
            print("YOU HAVE AN AXE")
    
        elif player["hasSword"]:
            print("YOU HAVE A HOOKED SWORD")
    
        else:
            print("STRAP IN")
    
        print("BEGIN BATTLE")

        #Battle
        
        roomStates["RoyalTomb"]["battleWon"] = True
        print("LET'S SAY YOU WON FOR NOW")
    
    else:
        print("YOU ALREADY DEFEATED THE BOSS")
    
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