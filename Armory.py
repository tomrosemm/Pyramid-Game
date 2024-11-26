def Armory(player, roomStates):
    
    directions = ["FORWARD", "Q"]    
    
    #Initialize the room states if not already done
    if "Armory" not in roomStates:
        roomStates["Armory"] = {"visited": False, "swordTaken": False}
        
    if not roomStates["Armory"]["visited"]:
        print("WELCOME TO THE ARMORY FOR THE FIRST TIME")
        roomStates["Armory"]["visited"] = True
    
    else:
        print("WELCOME BACK TO THE ARMORY")
    
    print("YOU ARE IN THE ARMORY")
    
    if not roomStates["Armory"]["swordTaken"]:
        swordChoice = input("TAKE SWORD? (y/n)").strip().upper()
    
        #Set up to catch mistaken entries, basically just a copy of the room movement structure
        if swordChoice == "Y":        
            player["hasSword"] = True
            roomStates["Armory"]["swordTaken"] = True
<<<<<<< Updated upstream
            print("SWORD TAKEN")
        
        else:     
            print("NO SWORD")
=======
            print("You take the sword in your free hand; its weight is reassuring.")
            print()

        elif swordChoice == "N":        
            player["hasTorch"] = False
            roomStates["Armory"]["swordTaken"] = False
            print("You decide against taking the sword, how brave.")
            print()
        while swordChoice != "Y" and swordChoice != "N":     
            print("Please enter a valid choice: (y/n)\n")
            input()
            print()

    else:
        print("The Armory is truly empty, now that you've taken the only sword.")
        print()
>>>>>>> Stashed changes
    
    else:
        print("THE SWORD HAS ALREADY BEEN TAKEN")
    
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