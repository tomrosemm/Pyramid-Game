from SandyCove import *

from Combat import *
    
def InnerBurialChamber(player, roomStates):
    
    directions = ["RIGHT", "BACKWARD", "Q"]
    
    #Initialize the room states if not already done
    if "InnerBurialChamber" not in roomStates:
        roomStates["InnerBurialChamber"] = {"visited": False, "battleWon": False}
        
    if not roomStates["Encampment"]["visited"]:
        print("WELCOME TO THE INNER BURIAL CHAMBER FOR THE FIRST TIME")
        roomStates["InnerBurialChamber"]["visited"] = True
    
    else:
        print("WELCOME BACK TO THE INNER BURIAL CHAMBER")
    
    print("YOU ARE IN THE INNER BURIAL CHAMBER")\
        
    if not roomStates["InnerBurialChamber"]["battleWon"]:
        print("YOU ARE ATTACKED BY 2 TOMB GOBLINS AND A MUMMY")
        
        if player["hasAxe"]:
            print("YOU HAVE AN AXE")
    
        else:
            print("STRAP IN")
        
        print("BEGIN BATTLE")
        
        #Battle
        
        roomStates["InnerBurialChamber"]["battleWon"] = True
        print("SUCCESSFUL BATTLE")
    
    else:
        print("YOU ALREADY DEFEATED THE ENEMIES")
        
    print("YOU CAN TRAVEL RIGHT OR BACKWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
        
    while userInput not in directions:
        print("CHOICES: RIGHT, BACKWARD")
        print("Q TO QUIT")
        userInput = input().strip().upper()
            
        if userInput == "RIGHT":
            print("RIGHT: TO SANDY COVE")#Test print
            SandyCove(player, roomStates)
        
        elif userInput == "BACKWARD":
            from SphinxRoom import SphinxRoom
            print("BACKWARD: TO SPHINX ROOM")
            SphinxRoom(player, roomStates)
                
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
    
    InnerBurialChamber(player, roomStates)