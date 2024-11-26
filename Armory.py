def Armory(player, roomStates):
    
    directions = ["FORWARD", "Q"]    
    
    #Initialize the room states if not already done
    if "Armory" not in roomStates:
        roomStates["Armory"] = {"visited": False, "swordTaken": False}
    
    print()
        
    if not roomStates["Armory"]["visited"]:
        print("You enter a small armory with empty weapon stands along the walls. There is a long stone table in the center.")
        print()
        roomStates["Armory"]["visited"] = True
    
    else:
        print("You return to the cramped armory.")
        print()
    
    if not roomStates["Armory"]["swordTaken"]:
        swordChoice = input("A long hooked blade sits upon the table, you notice as you move closer. Would you like to take it? (y/n)").strip().upper()
        print()
    
        #Set up to catch mistaken entries, basically just a copy of the room movement structure
        if swordChoice == "Y":        
            player["hasSword"] = True
            roomStates["Armory"]["swordTaken"] = True
            print("You take the sword in your free hand; its weight is reassuring.")
            print()
        
<<<<<<< Updated upstream
        else:     
            print("NO SWORD")
    
=======
        elif swordChoice == "N":        
            player["hasTorch"] = False
            roomStates["Armory"]["swordTaken"] = False
            print("You decide against taking the sword, how brave.")
            print()
            
        while swordChoice != "Y" and swordChoice != "N":     
            print("Please enter a valid choice: (y/n)\n")
            input()
            
        if swordChoice == "Y":        
            player["hasSword"] = True
            roomStates["Armory"]["swordTaken"] = True
            print("SWORD TAKEN")
        
        elif swordChoice == "N":        
            player["hasTorch"] = False
            roomStates["Armory"]["swordTaken"] = False
            print("You decide against taking the sword, how brave.")
            print()
>>>>>>> Stashed changes
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