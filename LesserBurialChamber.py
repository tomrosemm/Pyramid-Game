from SphinxRoom import *

from Combat import *

def LesserBurialChamber(player, roomStates):
    
    directions = ["FORWARD", "BACKWARD", "Q"]
    
    #Initialize the room states if not already done
    if "LesserBurialChamber" not in roomStates:
        roomStates["LesserBurialChamber"] = {"visited": False, "battleWon": False}
        
    if not roomStates["LesserBurialChamber"]["visited"]:
        print("FIRST TIME IN THE LESSER BURIAL CHAMBER")
        roomStates["LesserBurialChamber"]["visited"] = True
    
    else:
        print("WELCOME BACK TO THE LESSER BURIAL CHAMBER")
    
    print("YOU ARE IN THE LESSER BURIAL CHAMBER")
    
    if not roomStates["LesserBurialChamber"]["battleWon"]:
        print("TIME TO BATTLE!")
    
        #Battle
        
        roomStates["LesserBurialChamber"]["battleWon"] = True
    
        print("LET'S SAY YOU WON FOR NOW")
    
    else:
        print("YOU ALREADY DEFEATED THE ENEMIES HERE")
    
    print("YOU CAN TRAVEL FORWARD OR BACKWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
    
    while userInput not in directions:        
        print("CHOICE(S): FORWARD, BACKWARD")
        print("Q TO QUIT")
        userInput = input().strip().upper()

        if userInput == "FORWARD":   
            print("FORWARD: TO SPHINX ROOM") #Test Print
            SphinxRoom(player, roomStates)
        
        elif userInput == "BACKWARD":
            from SnakeWay import SnakeWay
            print("BACKWARD: TO SnakeWay")
            SnakeWay(player, roomStates)
            
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
    
    LesserBurialChamber(player, roomStates)