from SphinxRoom import *

from Combat import *

def LesserBurialChamber(player, roomStates):
    
    tombGoblin1 = {
        "name": "Goblin Fred",
        "health": 75,
        "damageRange": (5,15)
    }
    
    tombGoblin2 = {
        "name": "Goblin Fred",
        "health": 75,
        "damageRange": (5,15)
    }
    
    directions = ["FORWARD", "BACKWARD", "Q"]
    
    #Initialize the room states if not already done
    if "LesserBurialChamber" not in roomStates:
        roomStates["LesserBurialChamber"] = {"visited": False, "battleWon": False, "tombGoblin1Defeated": False, "tombGoblin2Defeated": False}
        
    if not roomStates["LesserBurialChamber"]["visited"]:
        print("FIRST TIME IN THE LESSER BURIAL CHAMBER")
        roomStates["LesserBurialChamber"]["visited"] = True
    
    else:
        print("WELCOME BACK TO THE LESSER BURIAL CHAMBER")
    
    print("YOU ARE IN THE LESSER BURIAL CHAMBER")
    
    if not roomStates["LesserBurialChamber"]["battleWon"]:
        print("TIME TO BATTLE!")

        roomStates["LesserBurialChamber"]["tombGoblin1Defeated"] = combat(player,tombGoblin1)
        roomStates["LesserBurialChamber"]["tombGoblin2Defeated"] = combat(player,tombGoblin2)
        
        if roomStates["LesserBurialChamber"]["tombGoblin1Defeated"] and roomStates["LesserBurialChamber"]["tombGoblin2Defeated"]:
            print("YOU WON!")
            roomStates["LesserBurialChamber"]["battleWon"] = True
        
        else:
            print("YOU WERE DEFEATED BY THE TOMB GOBLINS")
            print("GAME OVER")
            quit()
    
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