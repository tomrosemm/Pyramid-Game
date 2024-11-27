from SandyCove import *

from Combat import *
    
def InnerBurialChamber(player, roomStates):
    
    tombGoblin = {
        "name": "Goblin Fred",
        "health": 50,
        "damageRange": (3,10)
    }
    
    mummy = {
        "name": "The Mummy",
        "health": 75,
        "damageRange": (4, 10)
    }
    
    directions = ["RIGHT", "BACKWARD", "Q"]
    
    #Initialize the room states if not already done
    if "InnerBurialChamber" not in roomStates:
        roomStates["InnerBurialChamber"] = {"visited": False, "battleWon": False, "tombGoblinDefeated": False, "mummyDefeated": False}
        
    print()
        
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
            quit()
    
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