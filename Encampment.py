from SnakeWay import *

from Combat import *


def toSnakeway(player, roomStates):
    """!
    Contains code for moving from current room into the SnakeWay w/spacing and roomStates alteration
    """
    print()
    print("You move towards a small, dark cave-like passageway in the corner of the room.")
    SnakeWay(player, roomStates)


def toEntrance(player, roomStates):
    """!
    Contains code for moving from current room into the Entrance w/spacing and roomStates alteration
    """
    from Entrance import Entrance
    print()
    print("You decide to head back to the entrance")
    Entrance(player, roomStates)


def Encampment(player, roomStates):
    """!
    Contains the information and flow for the Encampment.
    Contains opportunity to take an axe, a battle with a tomb goblin, and movement forward and backward.
    
    @param          player          the player dictionary
    @param          roomStates      the roomStates dictionary
    @param          tombGoblin      the tombGoblin dictionary for the tomb goblin battled here
    @param          directions      list of directions available for travel
    @param          decisions       list of options available to choose
    @param          axeChoice       holds choice specific to taking axe
    @param          userInput       holds choice specific to room travel from this room
    """

    tombGoblin = {
        "name": "Goblin Fred",
        "health": 50,
        "damageRange": (3,10)
    }
    
    directions = ["FORWARD", "BACKWARD", "Q"]    
    decisions = ["Y", "N"]
    
    #Room Label
    print("____________________\n\nEncampment\n____________________\n")
    
    #Initialize the room states if not already done
    if "Encampment" not in roomStates:
        roomStates["Encampment"] = {"visited": False, "axeTaken": False, "battleWon": False}
        
    if not roomStates["Encampment"]["visited"]:
        print("You enter a small room. At the far end, rubble is piled up to form a makeshift, walled off tomb goblin camp.")
        print()
        roomStates["Encampment"]["visited"] = True
    
    else:
        print("You again enter the room with the makeshift goblin encampment.")
        print()
    
    #check if player has already taken the axe
    if not roomStates["Encampment"]["axeTaken"]:
        axeChoice = ''
        print("There is a splintered and battered axe on the floor of the room. Would you like to take it? (y/n)\n")
        
        while axeChoice not in decisions:
            
            axeChoice = input().strip().upper()
        
            if axeChoice == "Y":        
                player["hasAxe"] = True
                roomStates["Encampment"]["axeTaken"] = True
                print("\nYou pick up the axe. Though it has seen better days, the weapon will offer something in the way of protection.")
                print()

            elif axeChoice == "N":
                player["hasAxe"] = False
                roomStates["Encampment"]["axeTaken"] = False
                print("You decide against taking the axe. You don't need anything to slow you down!\n")

            else:
                print("Please enter a valid decision")
    
    else:
        print("It's a good thing you took the axe when you did; the tomb goblins blood has soaked the spot where it once lay.")
        print()
    
    if not roomStates["Encampment"]["battleWon"]:
        print("A snarling tomb goblin rushes at you.")
    
        roomStates["Encampment"]["battleWon"] = combat(player,tombGoblin)
        
        if roomStates["Encampment"]["battleWon"]:
            print()
            print("The tomb goblin lies dead at your feet.")
            print()
        
        else:
            print()
            print("You have been defeated by a single tomb goblin.")
            print()
            print("Game over; Goodbye.")
            exit(0)
    
    else:
        print("The dead tomb goblin lies near the door closest the entrance.")
        print()
    
    print("You can travel either forward or backward.")
    print("Where would you like to go?")
    print()
    userInput = ''
    
    while userInput not in directions:        
        print("Choices: forward, backward")
        print()
        print("Q to quit")
        print()
        userInput = input().strip().upper()

        if userInput == "FORWARD":
            toSnakeway(player,roomStates)
        
        elif userInput == "BACKWARD":
            toEntrance(player,roomStates)
            
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
    
    Encampment(player, roomStates)
