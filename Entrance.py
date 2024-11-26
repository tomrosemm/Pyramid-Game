from Encampment import *

def Entrance(player,roomStates):
    
    directions = ["FORWARD", "Q"]
    
    #Initialize the room states if not already done
    if "Entrance" not in roomStates:
        roomStates["Entrance"] = {"visited": False, "torchTaken": False}    
    
    if not roomStates["Entrance"]["visited"]:
        print("You find yourself in the corner of a pyramid. The way you entered has caved in.")
        print()
        roomStates["Entrance"]["visited"] = True
    
    else:
        print("You are in the room you entered the pyramid from.")
        print()
    
    #Check if player has already taken the torch
    if not roomStates["Entrance"]["torchTaken"]:
        torchChoice = input("There is a lit torch leaning against the corner of the room. Would you like to take it? (y/n)").strip().upper()
        print()
    
        #Set up to catch mistaken entries, basically just a copy of the room movement structure
        if torchChoice == "Y":        
            player["hasTorch"] = True
            roomStates["Entrance"]["torchTaken"] = True
            print("You pick up the torch, and feel a small sense of relief. At least you now have light.")
            print()
        
        else:     
            print("You decide against taking the torch. Who knows if you'll need to sneak around?")
            print()
    
    else:
        print("You grip your torch tightly, glad that you grabbed it earlier.")
        print()
    
    print("You can only travel forward from here.")
    # print()
    print("Where would you like to go?")
    print()
    userInput = ''
    
    while userInput not in directions:        
        print("CHOICE(S): FORWARD")
        print()
        print("Q TO QUIT")
        print()
        userInput = input().strip().upper()

        if userInput == "FORWARD":
            print()
            print("FORWARD: TO ENCAMPMENT") #Test Print
            
            if player["hasTorch"]:
                print()
                print("THE LIGHT OF THE TORCH GUIDES YOUR WAY")
                
            print("__________________________________________________")
            print()
            
            Encampment(player, roomStates)
        
        elif userInput == "Q":
            print()
            print("Goodbye")
            quit()
            
        else:
            print()
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
    
    Entrance(player, roomStates)