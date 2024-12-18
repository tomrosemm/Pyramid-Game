from SandyCove import *

from Combat import *

def InnerBurialChamber(player, roomStates):
    """!
    Contains the information and flow for the Inner Burial Chamber.
    Contains a battle with a tomb goblin and a mummy, and movement right and backward.
    
    @param          player          the player dictionary
    @param          roomStates      the roomStates dictionary
    @param          tombGoblin      the tombGoblin dictionary for the tomb goblin battled here
    @param          mummy           the mummy dictionary for the mummy battled here
    @param          directions      list of directions available for travel
    @param          userInput       holds choice specific to room travel from this room
    """
    
    tombGoblin = {
        "name": "Goblin Harold",
        "health": 50,
        "damageRange": (3,10)
    }
    
    mummy = {
        "name": "Ms. Mummy",
        "health": 75,
        "damageRange": (4, 10)
    }
    
    directions = ["RIGHT", "BACKWARD", "Q"]
    
    #Room Label
    print("____________________\n\nInner Burial Chamber\n____________________\n")
    
    #Initialize the room states if not already done
    if "InnerBurialChamber" not in roomStates:
        roomStates["InnerBurialChamber"] = {"visited": False, "battleWon": False, "tombGoblinDefeated": False, "mummyDefeated": False}
        
    if not roomStates["InnerBurialChamber"]["visited"]:
        print("You enter a mid sized room that must have once been well kept. There are remains of royal ornamentations ont he walls, and ornate sarcophagi reside in alcoves along the wall.")
        roomStates["InnerBurialChamber"]["visited"] = True
    
    else:
        print("You are once again in the Inner Burial Chamber.")
        
    print()
    
    if not roomStates["InnerBurialChamber"]["battleWon"]:
        print("You are attacked by a tomb goblin and a mummy! They seem wierdly close.")
        roomStates["InnerBurialChamber"]["tombGoblinDefeated"] = combat(player,tombGoblin)
        print()
        print("One down, one to go!")
        roomStates["InnerBurialChamber"]["mummyDefeated"] = combat(player,mummy)
        
        if roomStates["InnerBurialChamber"]["tombGoblinDefeated"] and roomStates["InnerBurialChamber"]["mummyDefeated"]:
            print("You defeated the tomb goblin and the mummy!")
            roomStates["InnerBurialChamber"]["battleWon"] = True
        
        else:
            print("You have been slain by the soon-to-be-wed mummy and tomb goblin. But, good for them at least, you know?")
            print()
            print("Game over; Goodbye.")
            exit(0)
    
    else:
        print("The defeated mummy and tomb goblin lay slumped against a wall in an eternal embrace.")

    print()    
    print("You can travel either right or backward.")
    print("Where would you like to go?")
    print()
    userInput = ''
    print()
        
    while userInput not in directions:
        print("Choices: right, backward")
        print()
        print("Q to quit")
        print()
        userInput = input().strip().upper()
        print()
            
        if userInput == "RIGHT":
            print("You head through the narrow gap in the cracked wall ahead.")
            print()
            print("__________________________________________________")
            SandyCove(player, roomStates)
        
        elif userInput == "BACKWARD":
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
    
    InnerBurialChamber(player, roomStates)
