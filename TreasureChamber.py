def TreasureChamber(player, roomStates):
    directions = ["BACKWARD", "Q"]   
    
    #Initialize the room states if not already done
    if "TreasureChamber" not in roomStates:
        roomStates["TreasureChamber"] = {"visited": False, "treasureTaken": False}
    
    print()
    
        
    if not roomStates["TreasureChamber"]["visited"]:
        print("WELCOME TO THE TREASURE CHAMBER FOR THE FIRST TIME")
        roomStates["TreasureChamber"]["visited"] = True
    
    else:
        print("WELCOME BACK TO THE TREASURE CHAMBER")
    
    print("YOU ARE IN THE TREASURE CHAMBER")
    
    if not roomStates["TreasureChamber"]["treasureTaken"]:
        treasureChoice = input("TAKE TREASURE? (y/n)").strip().upper()
    
        #Set up to catch mistaken entries, basically just a copy of the room movement structure
        if treasureChoice == "Y":
            roomStates["TreasureChamber"]["treasureTaken"] = True    
            print("TREASURE TAKEN. YOU WIN!")
            quit()

        elif treasureChoice == "N":
            roomStates["TreasureChamber"]["treasureTaken"] = False
            print("NO TREASURE")

        while treasureChoice != "Y" and treasureChoice != "N":     
            print("Please enter a valid choice: (y/n)\n")
            input()
            
        if treasureChoice == "Y":
            roomStates["TreasureChamber"]["treasureTaken"] = True    
            print("TREASURE TAKEN. YOU WIN!")
            quit()

        elif treasureChoice == "N":
            roomStates["TreasureChamber"]["treasureTaken"] = False
            print("NO TREASURE")

    else:
        print("THE TREASURE HAS ALREADY BEEN TAKEN")
    
    print("YOU CAN TRAVEL ONLY BACKWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
    
    while userInput not in directions:        
        print("CHOICE(S): BACKWARD")
        print("Q TO QUIT")
        userInput = input().strip().upper()

        if userInput == "BACKWARD":   
            from RoyalTomb import RoyalTomb
            print("BACKWARD: TO ROYAL TOMB") #Test Print
            RoyalTomb(player, roomStates)
            
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
    
    TreasureChamber(player, roomStates)