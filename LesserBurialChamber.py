from SphinxRoom import *

from Combat import *

def LesserBurialChamber(player, roomStates):
    """!
    Contains the information and flow for the Lesser Burial Chamber.
    Contains a battle with two tomb goblins, and movement forward and backward.
    
    @param          player          the player dictionary
    @param          roomStates      the roomStates dictionary
    @param          tombGoblin1     the tombGoblin dictionary for the first tomb goblin battled here
    @param          tombGoblin2     the tombGoblin dictionary for the second tomb goblin battled here
    @param          directions      list of directions available for travel
    @param          userInput       holds choice specific to room travel from this room
    """
    
    tombGoblin1 = {
        "name": "Goblin Ted",
        "health": 50,
        "damageRange": (3,10)
    }
    
    tombGoblin2 = {
        "name": "Goblin Greg",
        "health": 50,
        "damageRange": (3,10)
    }
    
    directions = ["FORWARD", "BACKWARD", "Q"]
    
    #Room Label
    print("____________________\n\nLesser Burial Chamber\n____________________\n")
    
    #Initialize the room states if not already done
    if "LesserBurialChamber" not in roomStates:
        roomStates["LesserBurialChamber"] = {"visited": False, "battleWon": False, "tombGoblin1Defeated": False, "tombGoblin2Defeated": False}
        
    if not roomStates["LesserBurialChamber"]["visited"]:
        print("You enter the Lesser Burial Chamber. Multiple dusty sarcophagi line both walls of the room, though the lids of the majority have been removed, revealing empty contents.")
        print()
        roomStates["LesserBurialChamber"]["visited"] = True
    
    else:
        print("You once again find yourself in the Lesser Burial Chamber.")
        print()
    
    if not roomStates["LesserBurialChamber"]["battleWon"]:
        print("The lids on the two sarcophagi that still have them are pushed aside, and you are charged by two tomb goblins.")
        print()

        roomStates["LesserBurialChamber"]["tombGoblin1Defeated"] = combat(player,tombGoblin1)
        print()
        print("One down, one to go!")
        roomStates["LesserBurialChamber"]["tombGoblin2Defeated"] = combat(player,tombGoblin2)
        
        if roomStates["LesserBurialChamber"]["tombGoblin1Defeated"] and roomStates["LesserBurialChamber"]["tombGoblin2Defeated"]:
            print("You defeated the tomb goblins!")
            roomStates["LesserBurialChamber"]["battleWon"] = True
        
        else:
            print("You have been slaughtered by the tomb goblins.")
            print()
            print("Game over; Goodbye.")
            exit(0)
    
    else:
        print()
        print("The dead tomb goblins lie piled atop one another... You didn't do that. Who did that?")
        print()
    
    print("You can travel either forward or backward.")
    print("Where would you like to go?")
    print()
    userInput = ''
    print()
    
    while userInput not in directions:        
        print("Choices: forward, backward")
        print()
        print("Q to quit")
        print()
        userInput = input().strip().upper()

        if userInput == "FORWARD":
            print()
            print("You move through a tall opening into the room of the sphinx.") #Test Print
            print("__________________________________________________")
            SphinxRoom(player, roomStates)
        
        elif userInput == "BACKWARD":
            print()
            from SnakeWay import SnakeWay
            print("You decide to return to the SnakeWay.")
            print("__________________________________________________")
            SnakeWay(player, roomStates)
            
        elif userInput == "Q":
            print()
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
    
    LesserBurialChamber(player, roomStates)
