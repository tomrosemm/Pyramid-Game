def Armory(player, roomStates):
    
    directions = ["FORWARD", "Q"]    
    decisions = ["Y", "N"]

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
        swordChoice = ''
        print("TAKE SWORD? (y/n)")

        while swordChoice not in decisions:

            swordChoice = input().strip().upper()

            #Set up to catch mistaken entries, basically just a copy of the room movement structure
            if swordChoice == "Y":        
                player["hasSword"] = True
                roomStates["Armory"]["swordTaken"] = True
                print("SWORD TAKEN\n")
            
            elif swordChoice == "N":        
                player["hasTorch"] = False
                roomStates["Armory"]["swordTaken"] = False
                print("You decide against taking the sword, how brave.")
                print()

            else:
                print("Please enter a valid decision\n")
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
<<<<<<< Updated upstream
            print("GOODBYE")
=======
            print("Goodbye.")
>>>>>>> Stashed changes
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