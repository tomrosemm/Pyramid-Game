from TreasureChamber import *

from Combat import *

def RoyalTomb(player, roomStates):
    
    mummy1 = {
        "name": "The Mummy",
        "health": 100,
        "damageRange": (3, 7)
    }
    
    mummy2 = {
        "name": "The Mummy",
        "health": 100,
        "damageRange": (3, 7)
    }

    directions = ["LEFT", "BACKWARD", "Q"]    
    
    #Initialize the room states if not already done
    if "RoyalTomb" not in roomStates:
        roomStates["RoyalTomb"] = {"visited": False, "battleWon": False, "mummy1Defeated": False, "mummy2Defeated": False}
        
    if not roomStates["RoyalTomb"]["visited"]:
        print("WELCOME TO THE ROYAL TOMB FOR THE FIRST TIME")
        roomStates["RoyalTomb"]["visited"] = True
    
    else:
        print("WELCOME BACK TO THE ROYAL TOMB")
    
    print("YOU ARE IN THE ROYAL TOMB")
    
    if not roomStates["RoyalTomb"]["battleWon"]:
        print("TIME TO BATTLE!")

        roomStates["RoyalTomb"]["mummy1Defeated"] = combat(player,mummy1)
        roomStates["RoyalTomb"]["mummy2Defeated"] = combat(player,mummy2)
        
        if roomStates["RoyalTomb"]["mummy1Defeated"] and roomStates["RoyalTomb"]["mummy2Defeated"]:
            print("YOU WON!")
            roomStates["RoyalTomb"]["battleWon"] = True
        
        else:
            print("YOU WERE DEFEATED BY THE ENEMIES")
            print("GAME OVER")
            quit()
    
    else:
        print("YOU ALREADY DEFEATED THE ENEMIES HERE")
    
    print("YOU CAN TRAVEL LEFT OR BACKWARD")
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
        "health": 200,
        "baseDamageRange": (10,20),
        "hasAxe": False,
        "hasSword": False,
        "axeBonus": (5, 10),
        "swordBonus": (10,15),
        "hasTorch": False
    }
    
    roomStates = {}
    
    RoyalTomb(player, roomStates)