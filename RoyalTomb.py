from TreasureChamber import *

from Combat import *

def RoyalTomb(player, roomStates):
    """!
    Contains the information and flow for the Royal Tomb.
    Contains a battle with two mummies, and movement left and backward.
    
    @param          player          the player dictionary
    @param          roomStates      the roomStates dictionary
    @param          mummy1          the mummy dictionary for the first mummy battled here
    @param          mummy2          the mummy dictionary for the second mummy battled here
    @param          directions      list of directions available for travel
    @param          userInput       holds choice specific to room travel from this room
    """
    
    mummy1 = {
        "name": "King Mummy",
        "health": 75,
        "damageRange": (4, 10)
    }
    
    mummy2 = {
        "name": "Queen Mummy",
        "health": 75,
        "damageRange": (4, 10)
    }

    directions = ["LEFT", "BACKWARD", "Q"]
    
    #Room Label
    print("____________________\n\nRoyal Tomb\n____________________\n")
    
    #Initialize the room states if not already done
    if "RoyalTomb" not in roomStates:
        roomStates["RoyalTomb"] = {"visited": False, "battleWon": False, "mummy1Defeated": False, "mummy2Defeated": False}
    
    print()
        
    if not roomStates["RoyalTomb"]["visited"]:
        print("You enter a room with a fewer number of sarcophagi than you've seen thus far, but much more lavishly adorned.")
        roomStates["RoyalTomb"]["visited"] = True
    
    else:
        print("You have returned to the Royal Tomb.")
    
    if not roomStates["RoyalTomb"]["battleWon"]:
        print("As you take your first steps into the room, two of the sarcophagi burst open, and you are attacked by two mummies.")

        roomStates["RoyalTomb"]["mummy1Defeated"] = combat(player,mummy1)
        print()
        print("One down, one to go!")
        roomStates["RoyalTomb"]["mummy2Defeated"] = combat(player,mummy2)
        
        if roomStates["RoyalTomb"]["mummy1Defeated"] and roomStates["RoyalTomb"]["mummy2Defeated"]:
            print("You defeated the pair of mummies!")
            print()
            roomStates["RoyalTomb"]["battleWon"] = True
        
        else:
            print("You were felled by the mummies. Try again!")
            print()
            print("Game over; Goodbye.")
            exit(0)
    
    else:
        print("The pair of mummies you defeated have dissapeared without a trace.")
        print()
    
    print("You can move left or backward.")
    print("Where would you like to go?")
    print()
    userInput = ''
    
    while userInput not in directions: 
        print()
        print("Choices: left, backward")
        print()
        print("Q to quit")
        print()
        userInput = input().strip().upper()
        print()

        if userInput == "LEFT":   
            print("You travel through the small, simple wooden door along the left side of the wall.")
            print()
            print("__________________________________________________")
            TreasureChamber(player, roomStates)
        
        elif userInput == "BACKWARD":
            from SandyCove import SandyCove
            print("You return to the Sandy Cove behind you.")
            print()
            print("__________________________________________________")
            SandyCove(player, roomStates)
            
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
    
    RoyalTomb(player, roomStates)
