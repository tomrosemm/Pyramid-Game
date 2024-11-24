from LesserBurialChamber import *

import random

#Do something to make coming back through the snakeway from sphinx room w/o torch also proc snake bites

def SnakeWay(player, roomStates):
    
    directions = ["FORWARD", "BACKWARD", "Q"]
    
    #Initialize the room states if not already done
    if "SnakeWay" not in roomStates:
        roomStates["Snakeway"] = {"visited": False}
    
    if not roomStates["Snakeway"]["visited"]:
        print("FIRST TIME IN THE SNAKEWAY")
        roomStates["Snakeway"]["visited"] = True
    
    else:
        print("WELCOME BACK TO THE SNAKEWAY")
    
    print("YOU ARE IN THE SNAKEWAY")
    
    if player["hasTorch"] == False:
        print("YOU DON'T HAVE A LIGHT SOURCE, AND IT'S PITCH BLACK. YOU HEAR HISSING")
            
    else:
        print("YOU HAVE A HANDY DANDY TORCH")
    
    print("YOU CAN TRAVEL FORWARD OR BACKWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
    
    while userInput not in directions:
        print("CHOICE(S): FORWARD, BACKWARD")
        print("Q TO QUIT")
        userInput = input().strip().upper()

        if userInput == "FORWARD":   
            print("FORWARD: TO LESSER BURIAL CHAMBER") #Test Print
            
            if player["hasTorch"]:
                print("THE LIGHT OF THE TORCH ALLOWS YOU TO COMPLETELY AVOID THE SNAKES")
            
            else:
                print("YOU STUMBLE THROUGH THE DARKNESS AND INTO MORE THAN A COUPLE SNAKES. THEY BITE.")
                #Take randomized damage
            
            LesserBurialChamber(player, roomStates)
        
        elif userInput == "BACKWARD":
            from Encampment import Encampment
            print("BACKWARD: TO ENCAMPMENT")
            Encampment(player, roomStates)
            
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
    
    SnakeWay(player, roomStates)
        