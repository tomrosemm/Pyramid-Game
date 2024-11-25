from Encampment import *

def Entrance(player,roomStates):
    
    #Setup some way to save what in this room has already happened, check against it before running combat
    
    directions = ["FORWARD"]    
    
    print("YOU ARE IN THE ENTRANCE")   
    torchChoice = input("TAKE TORCH? (y/n)").strip().upper()
    
    #Set up to catch mistaken entries, basically just a copy of the room movement structure
    if torchChoice == "Y":        
        player["hasTorch"] = True
        print("TORCH TAKEN")
    
    else:     
        print("NO TORCH")
    
    print("YOU CAN TRAVEL ONLY FORWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
    
    while userInput not in directions:        
        print("CHOICE(S): FORWARD")
        userInput = input().strip().upper()

        if userInput == "FORWARD":   
            print("FORWARD: TO ENCAMPMENT") #Test Print
            
            if player["hasTorch"]:
                print("THE LIGHT OF THE TORCH GUIDES YOUR WAY")
            
            Encampment(player)
            
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
    
    Entrance(player)