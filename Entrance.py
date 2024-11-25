from Encampment import *

def Entrance(player,roomStates):
    
    directions = ["FORWARD", "Q"]
    
    #Initialize the room states if not already done
    if "Entrance" not in roomStates:
        roomStates["Entrance"] = {"visited": False, "torchTaken": False}    
    
    if not roomStates["Entrance"]["visited"]:
        print("WELCOME TO THE PYRAMID")
        roomStates["Entrance"]["visited"] = True
    
    print("YOU ARE IN THE ENTRANCE")
    
    #Check if player has already taken the torch
    if not roomStates["Entrance"]["torchTaken"]:
        torchChoice = input("TAKE TORCH? (y/n)").strip().upper()
    
        #Set up to catch mistaken entries, basically just a copy of the room movement structure
        if torchChoice == "Y":        
            player["hasTorch"] = True
            roomStates["Entrance"]["torchTaken"] = True
            print("TORCH TAKEN")
        
        else:     
            print("NO TORCH")
    
    else:
        print("THE TORCH IS ALREADY TAKEN")
    
    print("YOU CAN TRAVEL ONLY FORWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
    
    while userInput not in directions:        
        print("CHOICE(S): FORWARD")
        print("Q TO QUIT")
        userInput = input().strip().upper()

        if userInput == "FORWARD":   
            print("FORWARD: TO ENCAMPMENT") #Test Print
            
            if player["hasTorch"]:
                print("THE LIGHT OF THE TORCH GUIDES YOUR WAY")
            
            Encampment(player, roomStates)
        
        elif userInput == "Q":
            print("Goodbye")
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
    
    Entrance(player, roomStates)