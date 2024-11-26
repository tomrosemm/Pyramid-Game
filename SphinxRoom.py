from Armory import *
from InnerBurialChamber import *

from Combat import *

import random

def SphinxRoom(player, roomStates):
    
    sphinxRiddleLibrary = {
        "riddle1": "ANSWER1",
        "riddle2": "ANSWER2",
        "riddle3": "ANSWER3"
    }

    directions = ["BACKWARD", "RIGHT", "Q"] #Changes if riddle is solved, as door is open
    
    # riddleAnswer = "THE ANSWER"
    
    #Initialize the room states if not already done
    if "SphinxRoom" not in roomStates:
        roomStates["SphinxRoom"] = {"visited": False, "riddleSolved": False, "riddleFailed": False}
        
    if not roomStates["SphinxRoom"]["visited"]:
        print("WELCOME TO THE ROOM TO THE SPHINX FOR THE FIRST TIME")
        roomStates["SphinxRoom"]["visited"] = True
    
    else:
        print("WELCOME BACK TO THE ROOM OF THE SPHINX")
    
    print("YOU ARE IN THE ROOM OF THE SPHINX")
    
    if not roomStates["SphinxRoom"]["riddleSolved"] and not roomStates["SphinxRoom"]["riddleFailed"]:
        print("A SPHINX GREETS YOU")
    
        if player["hasTorch"]:
            print("THE SPHINX SEEMS TO GREATLY ENJOY THE LIGHT OF THE TORCH")
    
        else:
            print("THE ROOM IS DIM AND MUSTY")
    
        print("THE SPHINX ASKS YOU A RIDDLE.")
        
        # Randomly pick a riddle and its answer
        riddle, riddleAnswer = random.choice(list(sphinxRiddleLibrary.items()))
        print(riddle)
        
        playerRiddleAnswer = input("YOUR ANSWER: ").strip().upper()
        
        if riddleAnswer == playerRiddleAnswer:
            print("YOU WERE CORRECT")
            roomStates["SphinxRoom"]["riddleSolved"] = True
            
            directions = ["FORWARD", "BACKWARD", "RIGHT", "Q"]
            
            if player["hasTorch"]:
                print("SPHINX THANKS YOU FOR THE LIGHT TOO.")
                #Give torch reward
                
            print("SPHINX CRUMBLES TO REVEAL A DOOR")
        
        else:
            print("YOU WERE WRONG")
            
            if player["hasTorch"]:
                print("SPHINX THANKS YOU FOR THE LIGHT THOUGH")
                #Give torch reward
            
            roomStates["SphinxRoom"]["riddleFailed"] = True
    
    elif roomStates["SphinxRoom"]["riddleSolved"]:
        print("THERE IS A CRUMBLED SPHINX ON THE FLOOR")
    
    elif roomStates["SphinxRoom"]["riddleFailed"]:
        print("THE SPHINX EYES YOU WITH DISTASTE")
    
    # print("YOU CAN TRAVEL " + ", ".join(directions))
    print("YOU CAN TRAVEL " + ", ".join([d for d in directions if d != "Q"]))
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
    
    while userInput not in directions:
        # print("CHOICES: " + ", ".join(directions).upper())
        print("CHOICES: " + ", ".join([d for d in directions if d != "Q"]).upper())
        print("Q TO QUIT")
        userInput = input().strip().upper()
        
        if userInput == "FORWARD" and roomStates["SphinxRoom"]["riddleSolved"]:
            print("YOU STEP OVER THE CRUMBLED SPHINX")
            print("FORWARD: TO ARMORY")#Test print
            Armory(player, roomStates)
        
        elif userInput == "FORWARD" and roomStates["SphinxRoom"]["riddleSolved"] == False:
                print("THE SPHINX GROWLS AS YOU APPROACH")
                #If there's time can we do something where you can push it further and enter an unbeatable battle with the sphinx?
        
        elif userInput == "RIGHT":
            print("RIGHT: TO INNER BURIAL CHAMBER") #Test print
            InnerBurialChamber(player, roomStates)
        
        elif userInput == "BACKWARD":
            from LesserBurialChamber import LesserBurialChamber
            print("BACKWARD: TO LESSER BURIAL CHAMBER")#Test print
            LesserBurialChamber(player, roomStates)
        
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
    
    SphinxRoom(player, roomStates)