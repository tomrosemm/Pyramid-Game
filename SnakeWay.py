from LesserBurialChamber import *

import random
import time

def SnakeWay(player, roomStates):
    """!
    Contains the information and flow for the SnakeWay.
    Contains snake bite danger, and movement forward and backward.
    """
    
    directions = ["FORWARD", "BACKWARD", "Q"]
    
    #Initialize the room states if not already done
    if "SnakeWay" not in roomStates:
        roomStates["SnakeWay"] = {"visited": False}
    
    print()
    
    if not roomStates["SnakeWay"]["visited"]:
        print("You enter the dark passageway, traversing the narrow cavern along the edge of the pyramid. ")
        print()
        roomStates["SnakeWay"]["visited"] = True
    
    else:
        print("You once again find yourself in the SnakeWay.")
        print()
        
    print("The SnakeWay is pitch black, and you hear a symphony of hisses from deeper in.")
    print()
    
    if player["hasTorch"] == True:
        print("You are quite glad that you grabbed the torch now.")
        print()
            
    else:
        print("You really regret not grabbing that torch now.")
        print()
    
    print("You can travel either forward or backward.")
    print("Where would you like to go?")
    print()
    userInput = ''
    
    while userInput not in directions:
        print("Choices: forward, backward")
        print()
        print("Q to quit")
        print()
        userInput = input().strip().upper()

        if userInput == "FORWARD" or userInput == "BACKWARD":
            
            
            if player["hasTorch"]:
                print()
                print("Thanks to the torch, you are able to navigate around the hissing snakes, avoiding their bites.")
                print()
            
            else:
                print()
                print("In absolute darkness, you stumble around the passage way, sustaining more than a couple snake bites..")
                print()
                
                #Take randomized damage
                i = 0
                while i < 3:
                    time.sleep(1)
                    snakeDamage = random.randint(1,5)
                    player["health"] -= snakeDamage
                    print("You are bitten by a snake, taking " + str(snakeDamage) + " damage.")
                    print()
                    i += 1
                    
                # print()
                
                input("You steady yourself and move on. Press enter to continue to the next room.")
                print()
                    
            if userInput == "FORWARD":
                print("You reach the end of the passageway and duck under a crumbling doorframe into the next room.")
                print()
                print("__________________________________________________")
            
                LesserBurialChamber(player, roomStates)
        
            elif userInput == "BACKWARD":
                from Encampment import Encampment
                print("You decide to turn back and revisit the tomb goblin encampment.")
                print()
                print("__________________________________________________")
                Encampment(player, roomStates)
            
        elif userInput == "Q":
            print("Goodbye.")
            break
            
        else:
            print("Please enter a valid direction.")

if __name__ == '__main__':
    
    player = {
        "name": "TestPlayer",
        "maxHealth": 100,
        "health": 100,
        "baseDamageRange": (10,20),
        "originalBaseDamageRange": (10,20),
        "hasAxe": False,
        "hasSword": False,
        "axeBonus": (5, 10),
        "swordBonus": (10,15),
        "hasTorch": False
    }
    
    roomStates = {}
    
    SnakeWay(player, roomStates)
            
