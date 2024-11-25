from SphinxRoom import *

def Armory(player):
    directions = ["FORWARD"]    
    
    print("YOU ARE IN THE ARMORY")   
    swordChoice = input("TAKE SWORD? (y/n)").strip().upper()
    
    #Set up to catch mistaken entries, basically just a copy of the room movement structure
    if swordChoice == "Y":        
        player["hasSword"] = True
        print("SWORD TAKEN")
    
    else:     
        print("NO SWORD")
    
    print("YOU CAN TRAVEL ONLY BACKWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
    
    while userInput not in directions:        
        print("CHOICE(S): BACKWARD")
        userInput = input().strip().upper()

        if userInput == "BACKWARD":   
            print("BACKWARD: TO SPHINX ROOM") #Test Print
            SphinxRoom(player)
            
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
    
    Armory(player)