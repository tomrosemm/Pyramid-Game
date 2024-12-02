def Armory(player, roomStates):
    """!
    Contains the information and flow for the Armory.
    Contains an opportunity to get a hooked sword, and movement backward. Doors seal after leaving first time.
    
    @param          player          the player dictionary
    @param          roomStates      the roomStates dictionary
    @param          directions      list of directions available for travel
    @param          decisions       list of options available to choose
    @param          swordChoice     holds choice specific to taking sword
    @param          userInput       holds choice specific to room travel from this room
    """
        
    directions = ["FORWARD", "Q"]    
    decisions = ["Y", "N"]
    
    #Room Label
    print("____________________\n\nArmory\n____________________\n")

    #Initialize the room states if not already done
    if "Armory" not in roomStates:
        roomStates["Armory"] = {"visited": False, "swordTaken": False}
        
    if not roomStates["Armory"]["visited"]:
        print("You enter a small armory with empty weapon stands along the walls. There is a long stone table in the center.")
        print()
        roomStates["Armory"]["visited"] = True
    
    else:
        print("You return to the cramped armory.")
        print()
    
    if not roomStates["Armory"]["swordTaken"]:

        swordChoice = ''
        print("A long hooked blade sits upon the table, you notice as you move closer. Would you like to take it? (y/n)")

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
        print("The Armory is truly empty, now that you've taken the only sword.")
        print()
    
    print("You can travel only backward.")
    print("Where would you like to go?")
    print()
    userInput = ''
    print()
    
    while userInput not in directions:        
        print("Choice: Backward")
        print()
        print('Q to quit')
        print()
        userInput = input().strip().upper()
        print()

        if userInput == "BACKWARD":
            from SphinxRoom import SphinxRoom
            print("You head back into the room of the sphinx.")
            print()
            print("__________________________________________________")
            SphinxRoom(player, roomStates)
            
        elif userInput == "Q":
            print("Goodbye.")
            quit()
            
        else:
            print("Please enter a valid direction.")

if __name__ == '__main__':
    
    #Test variables for launching straight from this room
    player = {
        "name": "TestPlayer",
        "maxHealth": 100,
        "health": 100,
        "baseDamageRange": (10,20),
        "originalBaseDamageRange": (10,20),
        "hasAxe": False,
        "hasSword": False,
        "axeBonus": (5, 10),
        "swordBonus": (10,15),
        "hasTorch": False
    }
    
    roomStates = {}
    
    Armory(player, roomStates)
