from SnakeWay import *

from Combat import *

def Encampment(player, roomStates):
    """!
    
    """
    
    tombGoblin = {
        "name": "Goblin Fred",
        "health": 50,
        "damageRange": (3,10)
    }
    
    directions = ["FORWARD", "BACKWARD", "Q"]    
    decisions = ["Y", "N"]
    #Initialize the room states if not already done
    if "Encampment" not in roomStates:
        roomStates["Encampment"] = {"visited": False, "axeTaken": False, "battleWon": False}
    
    print()
        
    if not roomStates["Encampment"]["visited"]:
        print("You enter a small room. At the far end, rubble is piled up to form a makeshift walled off encampment.")
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
        
            #Set up to catch mistaken entries, basically just a copy of the room movement structure
        
            if axeChoice == "Y":        
                player["hasAxe"] = True
                roomStates["Encampment"]["axeTaken"] = True
                print("You pick up the axe. Though it has seen better days, the weapon will offer something in the way of protection.")
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
            quit()
    
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
            print()
            print("You move towards a small, dark cave-like passageway in the corner of the room.")
            print("__________________________________________________")
            SnakeWay(player, roomStates)
        
        elif userInput == "BACKWARD":
            from Entrance import Entrance
            print()
            print("You decide to head back to the entrance")
            print("__________________________________________________")
            Entrance(player, roomStates)
            
        elif userInput == "Q":
            print()
            print("Goodbye.")
            quit()
            
        else:
            print("Please enter a valid direction.")

if __name__ == '__main__':
    """!
    
    """
    
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