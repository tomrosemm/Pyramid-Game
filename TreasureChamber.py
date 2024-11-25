def TreasureChamber(player, roomStates):
    directions = ["BACKWARD"]    
    
    print("YOU ARE IN THE TREASURE CHAMBER")   
    treasureChoice = input("TAKE TREASURE? (y/n)").strip().upper()
    
    #Set up to catch mistaken entries, basically just a copy of the room movement structure
    if treasureChoice == "Y":        
        print("TREASURE TAKEN. YOU WIN!")
        quit()
    
    else:     
        print("NO TREASURE")
    
    print("YOU CAN TRAVEL ONLY BACKWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
    
    while userInput not in directions:        
        print("CHOICE(S): BACKWARD")
        userInput = input().strip().upper()

        if userInput == "BACKWARD":   
            from RoyalTomb import RoyalTomb
            print("BACKWARD: TO ROYAL TOMB") #Test Print
            RoyalTomb(player, roomStates)
            
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
    
    TreasureChamber(player, roomStates)