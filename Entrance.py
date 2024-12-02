from Encampment import *


def toEncampment(player, roomStates):
    """!
    Contains code for moving from current room into the Encampment w/spacing and roomStates alteration
    """
    
    print()
    print("You move forward through the narrow doorway into the next room.")
    
    if player["hasTorch"]:
        print()
        print("The light of the torch guides your way.")
    
    Encampment(player, roomStates)
            

def Entrance(player, roomStates):
    """!
    Contains the information and flow for the Entrance room.
    Contains opportunity to take a torch, and movement forward.
    
    @param          player          the player dictionary
    @param          roomStates      the roomStates dictionary
    @param          directions      list of directions available for travel
    @param          decisions       list of options available to choose
    @param          torchChoice     holds choice specific to taking torch
    @param          userInput       holds choice specific to room travel from this room
    """
    
    #Holds the possible valid choices for decisions in the room
    directions = ["FORWARD", "Q"]
    decisions = ["Y", "N"]
    
    #Room Label
    print("____________________\n\nEntrance\n____________________\n")
    
    #Initialize the room state for Entrance if not already done
    if "Entrance" not in roomStates:
        roomStates["Entrance"] = {"visited": False, "torchTaken": False}    
    
    #If first time visiting room, welcome and set rooms visited value to True
    if not roomStates["Entrance"]["visited"]:
        print("You find yourself in the corner of a pyramid. The way you entered has caved in.")
        print()
        roomStates["Entrance"]["visited"] = True
    
    #If not first visit, welcome back to room
    else:
        print("You are again in the room you entered the pyramid from. The way you entered has caved in.")
        print()
    
    #Check if player has already taken the torch
    #If not, offer player the choice to do so
    if not roomStates["Entrance"]["torchTaken"]:
        
        #Holds user input that represents choice of whether to take torch or not
        torchChoice = ''
        print("There is a lit torch leaning against the corner of the room. Would you like to take it? (y/n)")

        #While loop to allow for erroneous input handling/looping until a valid input is found
        while torchChoice not in decisions:
            
            #Remove whitespace before/after input and force upper to bypass case-sensitivity
            torchChoice = input().strip().upper()
            
            if torchChoice == "Y":        
                player["hasTorch"] = True
                roomStates["Entrance"]["torchTaken"] = True
                print("You pick up the torch, and feel a small sense of relief. At least you now have light.\n")
                
            elif torchChoice == "N":        
                player["hasTorch"] = False
                roomStates["Entrance"]["torchTaken"] = False
                print("You decide against taking the torch. Who knows if you'll need to sneak around?")
                print()
                
            else:
                print("Please enter a valid decision\n")
            
    else:
        print("You grip your torch tightly, glad that you grabbed it earlier.")
        print()
    
    print("You can only travel forward from here.")
    print("Where would you like to go?")
    print()
    userInput = ''
    
    while userInput not in directions:        
        print("Choice: forward")
        print()
        print("Q to quit")
        print()
        userInput = input().strip().upper()

        if userInput == "FORWARD":
            toEncampment(player, roomStates)
        
        elif userInput == "Q":
            print()
            print("Goodbye.")
            quit()
            
        else:
            print()
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
    
    Entrance(player, roomStates)
