from SnakeWay import *

from Combat import *

def Encampment(player, roomStates):
    
    directions = ["FORWARD", "BACKWARD", "Q"]    
    
    #Initialize the room states if not already done
    if "Encampment" not in roomStates:
        roomStates["Encampment"] = {"visited": False, "axeTaken": False, "battleWon": False}
        
    if not roomStates["Encampment"]["visited"]:
        print("GREETINGS FROM THE TOMB GOBLINS")
        roomStates["Encampment"]["visited"] = True
    
    else:
        print("WELCOME BACK TO THE GOBLIN ENCAMPMENT")
    
    print("YOU ARE IN THE TOMB GOBLIN ENCAMPMENT")
    
    #check if player has already taken the axe
    if not roomStates["Encampment"]["axeTaken"]:
        axeChoice = input("TAKE AXE? (y/n)").strip().upper()
    
        #Set up to catch mistaken entries, basically just a copy of the room movement structure
        if axeChoice == "Y":        
            player["hasAxe"] = True
            roomStates["Encampment"]["axeTaken"] = True
            print("AXE TAKEN")
    
        else:     
            print("NO AXE")
    
    else:
        print("THE AXE HAS ALREADY BEEN TAKEN")
    
    if not roomStates["Encampment"]["battleWon"]:
        print("TIME TO BATTLE!")
    
        #Battle
    
        roomStates["Encampment"]["battleWon"] = True
    
        print("LET'S SAY YOU WON FOR NOW")
    
    else:
        print("YOU ALREADY DEFEATED THE TOMB GOBLINS")
    
    print("YOU CAN TRAVEL FORWARD OR BACKWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
    
    while userInput not in directions:        
        print("CHOICE(S): FORWARD, BACKWARD")
        print("Q TO QUIT")
        userInput = input().strip().upper()

        if userInput == "FORWARD":   
            print("FORWARD: TO SNAKEWAY") #Test Print
            SnakeWay(player, roomStates)
        
        elif userInput == "BACKWARD":
            from Entrance import Entrance
            print("BACKWARD: TO ENTRANCE")
            Entrance(player, roomStates)
            
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
    
    Encampment(player, roomStates)