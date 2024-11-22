def Armory(player, roomStates):
    
    #Setup some way to save what in this room has already happened, check against it before running combat
    
    directions = ["FORWARD", "Q"]    
    
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
        print('Q TO QUIT')
        userInput = input().strip().upper()

        if userInput == "BACKWARD":
            from SphinxRoom import SphinxRoom
            print("BACKWARD: TO SPHINX ROOM") #Test Print
            SphinxRoom(player, roomStates)
            
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
    
    Armory(player, roomStates)