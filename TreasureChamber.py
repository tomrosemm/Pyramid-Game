import time

def TreasureChamber(player, roomStates):
    directions = ["BACKWARD", "Q"]   
    
    #Initialize the room states if not already done
    if "TreasureChamber" not in roomStates:
        roomStates["TreasureChamber"] = {"visited": False, "treasureTaken": False}
    
    print()
        
    if not roomStates["TreasureChamber"]["visited"]:
        print("You enter through the wooden door into a small room with various jars and vials lining the shelves of the walls.")
        print("In the middle of the room is a small pedestal with a large, dark orb sitting on top.")
        roomStates["TreasureChamber"]["visited"] = True
    
    else:
        print("You have once again entered the Treasure Chamber.")
    
    print()
    
    if not roomStates["TreasureChamber"]["treasureTaken"]:
<<<<<<< Updated upstream
        treasureChoice = input("TAKE TREASURE? (y/n)").strip().upper()
    
        #Set up to catch mistaken entries, basically just a copy of the room movement structure
        if treasureChoice == "Y":
            roomStates["TreasureChamber"]["treasureTaken"] = True    
            print("TREASURE TAKEN. YOU WIN!")
            quit()
=======
        
        treasureChoice = ''
        print("The orb seems to draw you to it, and you oblige. Before you realize it, you are reaching towards it. Would you like to take the treasure of the pyramid? (y/n)\n")
        print()
>>>>>>> Stashed changes

        elif treasureChoice == "N":
            roomStates["TreasureChamber"]["treasureTaken"] = False
            print("NO TREASURE")

<<<<<<< Updated upstream
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
=======
            treasureChoice = input().strip().upper()
            print()

            #Set up to catch mistaken entries, basically just a copy of the room movement structure
            if treasureChoice == "Y":
                roomStates["TreasureChamber"]["treasureTaken"] = True    
                print("You take the orb, and before you know it you have been, somehow, launched through the roof of the pyramid and high, high into the air.")
                print()
                time.sleep(2)
                print("You have enough time to think over your life and the decisions that lead you here as you fall to your inevitable fate.")
                print()
                time.sleep(2)
                print("You could have been something. You could have taken that corner office job in Stacy's dad's company, but no. You were too proud.")
                print()
                time.sleep(2)
                print("You wonder if you'll be identifiable. Part of you assumes you'll just be a we spot on the sand, but stranger things-")
                print()
                time.sleep(2)
                print("Splat!")
                time.sleep(5)
                print("You win!")
                time.sleep(3)
                quit()

            elif treasureChoice == "N":
                roomStates["TreasureChamber"]["treasureTaken"] = False
                print("At the last moment, you use your other hand to yank back the one reaching toward the orb. Not yet.")
                print()
            
            else:
                print("Please enter a valid decision.\n")
>>>>>>> Stashed changes

    else:
        print("You have somehow taken the orb and lived to tell the tale.")
        print()
    
    print("You can travel only backward.")
    print("Where would you like to go?")
    print()
    userInput = ''
    
    while userInput not in directions:
        print()    
        print("Choice: backward")
        print()
        print("Q to quit")
        print()
        userInput = input().strip().upper()
        print()

        if userInput == "BACKWARD":   
            from RoyalTomb import RoyalTomb
            print("You head back into the royal tomb.")
            print()
            print("__________________________________________________")
            RoyalTomb(player, roomStates)
            
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
    
    TreasureChamber(player, roomStates)