from Armory import *
from InnerBurialChamber import *

from Combat import *

import random

def SphinxRoom(player, roomStates):
    
    sphinxRiddleLibrary = {
        "What is that which in the morning goes upon four feet, upon two feet in the afternoon, and in the evening upon three?": "MAN",
        "I am the dark child of a shining father, a wingless bird flying to heaven; every eye that meets me weeps, but not from grief. What am I?": "SMOKE",
        "Always wax, yet always wane: I melt, succumbed to the flame. Lighting darkness, with fate unblessed, I soon devolve to shapeless mess. What am I? : A [Blank]": "CANDLE"  
    }

    directions = ["BACKWARD", "RIGHT", "Q"] #Changes if riddle is solved, as door is open
    
    # riddleAnswer = "THE ANSWER"
    
    #Initialize the room states if not already done
    if "SphinxRoom" not in roomStates:
        roomStates["SphinxRoom"] = {"visited": False, "riddleSolved": False, "riddleFailed": False}
    
    print()
        
    if not roomStates["SphinxRoom"]["visited"]:
        print("You enter a large hall, at the end of which sits a sphinx, largely in ruin; only his head remains.")
        print()
        roomStates["SphinxRoom"]["visited"] = True
    
    else:
        print("You enter the room of the sphinx, the long hall stretching on into the shadows.")
        print()
    
    if not roomStates["SphinxRoom"]["riddleSolved"] and not roomStates["SphinxRoom"]["riddleFailed"]:
        print("As you approach the large sphinx, she eyes you sharply, and you wisely stop outside his reach.")
        print()
    
        if player["hasTorch"]:
            print("As the light of the torch illuminates the sphinx, you can't help but think he looks slightly pleased by it. He begins to speak.")
            print()
    
        else:
            print("The darkness of the room envelopes you, as the sphinx begins to speak from the shadows.")
            print()
    
        print(f"Greetings, {player['name']}. I see your travels have landed you in some trouble. I can help you be stronger, but first you must solve my riddle.")
        print()
        
        # Randomly pick a riddle and its answer
        riddle, riddleAnswer = random.choice(list(sphinxRiddleLibrary.items()))
        print(riddle)
        print()
        
        playerRiddleAnswer = input("Your answer: ").strip().upper()
        
        if riddleAnswer == playerRiddleAnswer:
            print("The sphinx is pleased, and says 'Correct!'")
            print()
            roomStates["SphinxRoom"]["riddleSolved"] = True
            
            directions = ["FORWARD", "BACKWARD", "RIGHT", "Q"]
            
            if player["hasTorch"]:
                print("'Thank you for the light of that torch as well; it's so dark in here, one could easily go mad. Let me heal you.'")
                print()
                
                if player["health"] < 100:
                    player["health"] = 100
                    print("You have been fully healed!")
                    print()
                
                else:
                    print("Oh my... you are already at full health? Now how'd you do that?")
                    print()
                
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