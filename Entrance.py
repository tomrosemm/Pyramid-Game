from Encampment import *

def Entrance(player, roomStates):
    
    directions = ["FORWARD", "Q"]
    decisions = ["Y", "N"]
    #Initialize the room states if not already done
    if "Entrance" not in roomStates:
        roomStates["Entrance"] = {"visited": False, "torchTaken": False}    
    
    if not roomStates["Entrance"]["visited"]:
        print("You find yourself in the corner of a pyramid. The way you entered has caved in.")
        print()
        roomStates["Entrance"]["visited"] = True
    
    else:
        print("You are in the room you entered the pyramid from. The way you entered has caved in.")
        print()
    
    #Check if player has already taken the torch
    if not roomStates["Entrance"]["torchTaken"]:
        torchChoice = ''
        print("There is a lit torch leaning against the corner of the room. Would you like to take it? (y/n)")

        while torchChoice not in decisions:
            
            torchChoice = input().strip().upper()

            #Set up to catch mistaken entries, basically just a copy of the room movement structure
            
            if torchChoice == "Y":        
                player["hasTorch"] = True
                roomStates["Entrance"]["torchTaken"] = True
                print("You pick up the torch, and feel a small sense of relief. At least you now have light.\n")
                
            elif torchChoice == "N":        
                player["hasTorch"] = False
                roomStates["Entrance"]["torchTaken"] = False
                print("You decide against taking the torch. Who knows if you'll need to sneak around?")
                print()
                
            else:
                print("Please enter a valid decision\n")
            
    else:
        print("You grip your torch tightly, glad that you grabbed it earlier.")
        print()
    
    print("You can only travel forward from here.")
    # print()
    print("Where would you like to go?")
    print()
    userInput = ''
    
    while userInput not in directions:        
        print("Choice: forward")
        print()
        print("Q to quit")
        print()
        userInput = input().strip().upper()

        if userInput == "FORWARD":
            print()
            print("You move forward through the narrow doorway into the next room.")
            
            if player["hasTorch"]:
                print()
                print("The light of the torch guides your way.")
                
            print("__________________________________________________")
            
            Encampment(player, roomStates)
        
        elif userInput == "Q":
            print()
            print("Goodbye.")
            break
            
        else:
            print()
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
    
    Entrance(player, roomStates)
