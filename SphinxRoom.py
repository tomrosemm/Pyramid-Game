from Armory import *
from InnerBurialChamber import *

from Combat import *

import random
import time

def SphinxRoom(player, roomStates):
    """!
    Contains the information and flow for the Sphinx Room.
    Contains a sphinx with a riddle that can reveal door to the armory as well as heal, and movement forward, right, and backward.
    """

    #List of riddles and their respective answers
    sphinxRiddleLibrary = {
        "What is that which in the morning goes upon four feet, upon two feet in the afternoon, and in the evening upon three?": "MAN",
        "I am the dark child of a shining father, a wingless bird flying to heaven; every eye that meets me weeps, but not from grief. What am I?": "SMOKE",
        "Always wax, yet always wane: I melt, succumbed to the flame. Lighting darkness, with fate unblessed, I soon devolve to shapeless mess. What am I? : A [Blank]": "CANDLE",  
        "I run, but never walk; I murmur but never talk; I have a bed but never sleep; I have a mouth but never eat. What am I?: A [Blank]": "RIVER",
        "I cannot be seen or felt, nor heard or smelt; The more I am, the less you see; The sooner the Sun fades, the greater I'll be. What am I?": "DARKNESS",
        "The wind is a good friend of mine, I was very popular in the dawn of time. I'll be with you in your times of fear, but if you say my name I will disappear. What am I?": "SILENCE",
        "I have a tail but no body, I have a head but no brain. What am I?: A [Blank]": "COIN"
    }

    directions = ["BACKWARD", "RIGHT", "Q"] #Changes if riddle is solved, as door is open
    
    #Initialize the room states if not already done
    if "SphinxRoom" not in roomStates:
        roomStates["SphinxRoom"] = {"visited": False, "riddleSolved": False, "riddleFailed": False}
    
    print()
        
    if not roomStates["SphinxRoom"]["visited"]:
        print("You enter a large hall, at the end of which sits a sphinx, largely in ruin; only his head remains.")
        print()
        roomStates["SphinxRoom"]["visited"] = True
    
    else:
        print("You enter the room of the sphinx, the long hall stretching on into the shadows.")
        print()
    
    if not roomStates["SphinxRoom"]["riddleSolved"] and not roomStates["SphinxRoom"]["riddleFailed"]:
        print("As you approach the large sphinx, he eyes you sharply, and you wisely stop outside his reach.")
        print()
    
        if player["hasTorch"]:
            print("As the light of the torch illuminates the sphinx, you can't help but think he looks slightly pleased by it. He begins to speak.")
            print()
    
        else:
            print("The darkness of the room envelopes you, as the sphinx begins to speak from the shadows.")
            print()
    
        print(f"'Greetings, {player['name']}. I see your travels have landed you in some trouble. I can help you be stronger, but first you must solve my riddle.'")
        print()
        
        # Randomly pick a riddle and its answer
        riddle, riddleAnswer = random.choice(list(sphinxRiddleLibrary.items()))
        print("'" + riddle + "'")
        print()
        
        playerRiddleAnswer = input("Your answer: ").strip().upper()
        print()
        
        if riddleAnswer == playerRiddleAnswer:
            print("The sphinx is pleased, and says 'Correct!'")
            print()
            roomStates["SphinxRoom"]["riddleSolved"] = True
            
            directions = ["FORWARD", "BACKWARD", "RIGHT", "Q"]
            
            if player["hasTorch"]:
                print("'Thank you for the light of that torch as well; it's so dark in here, one could easily go mad. Let me heal you.'")
                print()
                
                if player["health"] < 100:
                    player["health"] = 100
                    print("You have been fully healed!")
                    print()
                
                else:
                    print("Oh my... you are already at full health? Now how'd you do that?")
                    print()
                
            print("Once towering with wisdom and riddles, the sphinx watched in silent despair as its once-pristine stone cracked, each fragment carrying centuries of memory.")
            print()
            time.sleep(2)
            print("As the final piece fell, its voice—a whisper of ancient secrets—faded into the wind, unheard and unremembered.")
            print()
            time.sleep(2)
            print("Alone in the rubble, it mourned not its end, but the noble purpose it could never fulfill again.")
            print()
            time.sleep(4)
            print("There was a door behind the sphinx!")
            print()
            time.sleep(1)
        
        else:
            print("The sphinx sadly lowers his gaze. 'I'm sorry, that's wrong. I would love to help you, but my aid comes with a price.'")
            print()
            
            if player["hasTorch"]:
                print("'I do thank you for the gift of the light though. That counts for something.''")
                print()
                
                if player["health"] < player["maxHealth"]:
                    amountHealed = player["maxHealth"] - player["health"]
                    player["health"] = player["maxHealth"]
                    print()
                    print("You recovered " + str(amountHealed) + " hit points.")
                    print()
                
                else:
                    print("Oh my... you are already at full health? Now how'd you do that?")
                    print()
            
            roomStates["SphinxRoom"]["riddleFailed"] = True
    
    elif roomStates["SphinxRoom"]["riddleSolved"]:
        print("The remains of the sphinx head lie scattered on the floor, rendered dust in the winds of time.")
        print()
    
    elif roomStates["SphinxRoom"]["riddleFailed"]:
        print("As you move past, the sphinx watches you with pity.")
        print()
    
    print("You can go " + ", ".join([d for d in directions if d != "Q"]).lower())
    print("Where would you like to go?")
    print()
    userInput = ''
    
    while userInput not in directions:
        print("Choices: " + ", ".join([d for d in directions if d != "Q"]).lower())
        print()
        print("Q to quit")
        print()
        userInput = input().strip().upper()
        print()
        
        if userInput == "FORWARD" and roomStates["SphinxRoom"]["riddleSolved"]:
            print("You step over the crumbled sphinx, and make your way into the small door that was behind him.")
            print()
            print("__________________________________________________")
            Armory(player, roomStates)
        
        elif userInput == "RIGHT":
            print("You make your way through the ornate door at the end of the hall nearest the sphinx.")
            print()
            print("__________________________________________________")
            InnerBurialChamber(player, roomStates)
        
        elif userInput == "BACKWARD":
            from LesserBurialChamber import LesserBurialChamber
            print("You head back through the door to the Lesser Burial Chamber.")
            print()
            print("__________________________________________________")
            LesserBurialChamber(player, roomStates)
        
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
    
    SphinxRoom(player, roomStates)
