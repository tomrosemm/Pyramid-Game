from Encampment import *

def Entrance(player,roomStates):
    
    directions = ["FORWARD", "Q"]
    
    #Initialize the room states if not already done
    if "Entrance" not in roomStates:
        roomStates["Entrance"] = {"visited": False, "torchTaken": False}    
    
    if not roomStates["Entrance"]["visited"]:
        print("WELCOME TO THE PYRAMID")
        print()
        roomStates["Entrance"]["visited"] = True
    
    print("YOU ARE IN THE ENTRANCE")
    print()
    
    #Check if player has already taken the torch
    if not roomStates["Entrance"]["torchTaken"]:
        torchChoice = input("TAKE TORCH? (y/n)").strip().upper()
        print()
    
        #Set up to catch mistaken entries, basically just a copy of the room movement structure
        if torchChoice == "Y":        
            player["hasTorch"] = True
            roomStates["Entrance"]["torchTaken"] = True
            print("TORCH TAKEN")
            print()
        
        else:     
            print("NO TORCH")
            print()
    
    else:
        print("THE TORCH IS ALREADY TAKEN")
        print()
    
    print("YOU CAN TRAVEL ONLY FORWARD")
    print()
    print("WHERE DO YOU WANT TO MOVE?")
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