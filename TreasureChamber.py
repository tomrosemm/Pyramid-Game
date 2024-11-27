def TreasureChamber(player, roomStates):
    
    directions = ["BACKWARD", "Q"]   
    decisions = ["Y", "N"]

    #Initialize the room states if not already done
    if "TreasureChamber" not in roomStates:
        roomStates["TreasureChamber"] = {"visited": False, "treasureTaken": False}
        
    if not roomStates["TreasureChamber"]["visited"]:
        print("WELCOME TO THE TREASURE CHAMBER FOR THE FIRST TIME")
        roomStates["TreasureChamber"]["visited"] = True
    
    else:
        print("WELCOME BACK TO THE TREASURE CHAMBER")
    
    print("YOU ARE IN THE TREASURE CHAMBER")
    
    if not roomStates["TreasureChamber"]["treasureTaken"]:
        
        treasureChoice = ''
        print("Take treasure? (y/n)\n")

        while treasureChoice not in decisions:

            treasureChoice = input().strip().upper()

            #Set up to catch mistaken entries, basically just a copy of the room movement structure
            if treasureChoice == "Y":
                roomStates["TreasureChamber"]["treasureTaken"] = True    
<<<<<<< Updated upstream
                print("TREASURE TAKEN. YOU WIN!")
=======
                print("You take the orb, and before you know it you have been, somehow, launched through the roof of the pyramid and high, high into the air.")
                print()
                time.sleep(4)
                print("You have enough time to think over your life and the decisions that lead you here as you fall to your inevitable fate.")
                print()
                time.sleep(4)
                print("You could have been something. You could have taken that corner office job in Stacy's dad's company, but no. You were too proud.")
                print()
                time.sleep(4)
                print("You wonder if you'll be identifiable. Part of you assumes you'll just be a we spot on the sand, but stranger things-")
                print()
                time.sleep(3)
                print("Splat!")
                print()
                time.sleep(4)
                print("You win!")
                time.sleep(3)
>>>>>>> Stashed changes
                quit()

            elif treasureChoice == "N":
                roomStates["TreasureChamber"]["treasureTaken"] = False
                print("NO TREASURE")
            
            else:
                print("Please enter a valid decision\n")

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
<<<<<<< Updated upstream
            print("GOODBYE")
=======
            print("Goodbye.")
>>>>>>> Stashed changes
            quit()
            
        else:
            print("Please enter a valid direction.\n")

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