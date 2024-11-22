from SnakeWay import *

from Combat import *

def Encampment(player, roomStates):
    
    #Setup some way to save that combat in this room has already happened, check against it before running combat
    
    directions = ["FORWARD", "BACKWARD", "Q"]    
    
    print("YOU ARE IN THE TOMB GOBLIN ENCAMPMENT")   
    axeChoice = input("TAKE AXE? (y/n)").strip().upper()
    
    #Set up to catch mistaken entries, basically just a copy of the room movement structure
    if axeChoice == "Y":        
        player["hasAxe"] = True
        print("AXE TAKEN")
    
    else:     
        print("NO AXE")
    
    print("TIME TO BATTLE!")
    print("LET'S SAY YOU WON FOR NOW")
    
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