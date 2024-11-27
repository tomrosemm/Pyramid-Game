from RoyalTomb import *

def SandyCove(player, roomStates):
    """!
    Contains the information and flow for the Sandy Cove.
    Contains an event with goddess Isis, the opportunity for healing, item hints, and unlocking the sphinx's riddle once more, and movement forward and backward.
    
    @param          player          the player dictionary
    @param          roomStates      the roomStates dictionary
    @param          directions      list of directions available for travel
    @param          amountHealed    reflects the amount of damage healed by Isis
    @param          userInput       holds choice specific to room travel from this room
    """
    
    directions = ["FORWARD", "BACKWARD", "Q"]
    
    #Initialize the room states if not already done
    if "SandyCove" not in roomStates:
        roomStates["SandyCove"] = {"visited": False, "isisEventOccurred": False, "receivedFullBlessings": False}
    
    print()
    
    if not roomStates["SandyCove"]["visited"]:
        print("You squeeze through the crack in the wall to find a large, open room.")
        print("Mounds of sand are piled high against the walls, and there is, somehow, vibrant shrubbery littered throughout the room.")
        roomStates["SandyCove"]["visited"] = True
    
    print()
    
    if not roomStates["SandyCove"]["isisEventOccurred"]:
        print("As you enter, you draw the attention of a tall, slender woman resting at a bench in the middle of the room.")
        print("She is wearing a sheath dress, resting a staff of papyrus across her lap, and wearing a headpiece shaped like a throne.")
        print()
        print("As you approach, you see she is observing you with a smile, though there is a sadness in her eyes.")
        print()
        print(f"'Welcome, {player['name']}. I know you have faced many harsh trials to reach this place, but rest easy; I'm here to offer you wisdom and protection.'")
        roomStates["SandyCove"]["isisEventOccurred"] = True
        print()

        if player["health"] < player["maxHealth"]:
            print("'Allow me to first offer my blessing' she says, as she places a hand on your shoulder. You feel your strength return to you in full.'")
            amountHealed = player["maxHealth"] - player["health"]
            player["health"] = player["maxHealth"]
            print()
            print("You recovered " + str(amountHealed) + " hit points.")

        else:
            print("'No seriously, what bug did you find? How are you at full health, that shouldn't even be possible, let alone easy.'")
        
        print()

        if not roomStates["SandyCove"]["receivedFullBlessings"]:
            if player["hasTorch"] == False:
                print("'You have missed a tool at the beginning of your journey that may yet continue to assist you in your endeavors. Head back to the first room you entered.'")
                print()
                #Option to send player to room? Just adding item feels weak
                
            elif player["hasAxe"] == False:
                print("'You have missed an opportunity to strengthen yourself. Head back to the room you first entered combat in.'")
                print()
                #Option to send player to room? Just adding item feels weak
                
            elif player["hasTorch"] and player["hasAxe"] and roomStates["SphinxRoom"]["riddleFailed"]:
                print("'The sphinx likes his riddles, but he's usually bound to archaic rules. I can bend them just a little, so let's give you another shot at that riddle.'")
                print()
                #Keep track of this occuring in roomStates so player can't endlessly loop into the riddle
                roomStates["SphinxRoom"]["riddleSolved"] = False
                roomStates["SphinxRoom"]["riddleFailed"] = False
                #Option to send player to room?
        
        else:
            print("'I have helped you all I can. Go, and be strong little one.'")
            roomStates["SandyCove"]["receivedFullBlessings"] = True

    else:
        print("The woman on the bench nods at you as you enter, but makes no other greeting. She seems weaker than before.")
    
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
        print()
        
        if userInput == "FORWARD":
            print("You head through the large, gold encrusted door in front of you.")
            print()
            print("__________________________________________________")
            RoyalTomb(player, roomStates)
        
        elif userInput == "BACKWARD":
            from InnerBurialChamber import InnerBurialChamber
            print("You return to the Inner Burial Chamber.")
            print()
            print("__________________________________________________")
            InnerBurialChamber(player, roomStates)
            
        elif userInput == "Q":
            print("Goodbye.")
            break
        
        else:
            print("Please enter a valid direction.")

if __name__ == '__main__':
    
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
    
    SandyCove(player, roomStates)
