from SandyCove import *

from Combat import *
    
def InnerBurialChamber(player, roomStates):
    
    tombGoblin = {
        "name": "Goblin Fred",
        "health": 75,
        "damageRange": (5,15)
    }
    
    mummy = {
        "name": "The Mummy",
        "health": 100,
        "damageRange": (3, 7)
    }
    
    directions = ["RIGHT", "BACKWARD", "Q"]
    
    #Initialize the room states if not already done
    if "InnerBurialChamber" not in roomStates:
        roomStates["InnerBurialChamber"] = {"visited": False, "battleWon": False, "tombGoblinDefeated": False, "mummyDefeated": False}
        
    if not roomStates["InnerBurialChamber"]["visited"]:
        print("WELCOME TO THE INNER BURIAL CHAMBER FOR THE FIRST TIME")
        roomStates["InnerBurialChamber"]["visited"] = True
    
    else:
        print("WELCOME BACK TO THE INNER BURIAL CHAMBER")
    
    print("YOU ARE IN THE INNER BURIAL CHAMBER")\
        
    if not roomStates["InnerBurialChamber"]["battleWon"]:
        print("TIME TO BATTLE!")

        roomStates["InnerBurialChamber"]["tombGoblinDefeated"] = combat(player,tombGoblin)
        roomStates["InnerBurialChamber"]["mummyDefeated"] = combat(player,mummy)
        
        if roomStates["InnerBurialChamber"]["tombGoblinDefeated"] and roomStates["InnerBurialChamber"]["mummyDefeated"]:
            print("YOU WON!")
            roomStates["InnerBurialChamber"]["battleWon"] = True
        
        else:
            print("YOU WERE DEFEATED BY THE ENEMIES")
            print("GAME OVER")
            quit()
    
    else:
        print("YOU ALREADY DEFEATED THE ENEMIES HERE")
        
    print("YOU CAN TRAVEL RIGHT OR BACKWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
        
    while userInput not in directions:
        print("CHOICES: RIGHT, BACKWARD")
        print("Q TO QUIT")
        userInput = input().strip().upper()
            
        if userInput == "RIGHT":
            print("RIGHT: TO SANDY COVE")#Test print
            SandyCove(player, roomStates)
        
        elif userInput == "BACKWARD":
            from SphinxRoom import SphinxRoom
            print("BACKWARD: TO SPHINX ROOM")
            SphinxRoom(player, roomStates)
                
        elif userInput == "Q":
            print("GOODBYE")
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
    
    InnerBurialChamber(player, roomStates)