from SnakeWay import *
from InnerBurialChamber import *

def SphinxRoom(player):
    
    directions = ["BACKWARD", "RIGHT"] #Changes if riddle is solved, as door is open
    
    riddleAnswer = "THE ANSWER"
    
    print("YOU ARE IN THE ROOM OF THE SPHINX")
    
    print("A SPHINX GREETS YOU")
    
    if player["hasTorch"]:
        print("THE SPHINX SEEMS TO GREATLY ENJOY THE LIGHT OF THE TORCH")
    
    else:
        print("THE ROOM IS DIM AND MUSTY")
    
    print("THE SPHINX ASKS YOU A RIDDLE. THE ANSWER IS: THE ANSWER")
    playerRiddleAnswer = ''
    playerRiddleAnswer = input().strip().upper()#Depending on the answer might not want strip here
    
    if riddleAnswer == playerRiddleAnswer:
        print("YOU WERE CORRECT")
        
        if player["hasTorch"]:
            print("SPHINX THANKS YOU FOR THE LIGHT TOO.")
            #Give torch reward
        
        print("SPHINX CRUMBLES TO REVEAL A DOOR")
        riddleSolved = True
        directions = ["forward", "backward", "right"]
    
    else:
        print("YOU WERE WRONG")
        
        if player["hasTorch"]:
            print("SPHINX THANKS YOU FOR THE LIGHT THOUGH")
            #Give torch reward
        
        riddleSolved = False
    
    print("YOU CAN TRAVEL " + ", ".join(directions))
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
    
    while userInput not in directions:
        print("CHOICES: " + ", ".join(directions).upper())
        userInput = input().strip().upper
        
        if userInput == "FORWARD" & riddleSolved:
            print("YOU STEP OVER THE CRUMBLED SPHINX")
            print("FORWARD: TO ARMORY")#Test print
            #Armory(player)
        
        elif userInput == "FORWARD" & riddleSolved == False:
                print("THE SPHINX GROWLS AS YOU APPROACH")
                #If there's time can we do something where you can push it further and enter an unbeatable battle with the sphinx?
        
        elif userInput == "RIGHT":
            print("RIGHT: TO INNER BURIAL CHAMBER") #Test print
            InnerBurialChamber(player)
        
        elif userInput == "BACKWARD":
            print("BACKWARD: TO SNAKEWAY")#Test print
            SnakeWay(player)
        
        else:
            print("Please enter a valid direction.")

if __name__ == '__main__':
    
    player = {
        "name": "Player",
        "health": 100,
        "baseDamageRange": (10,20),
        "hasAxe": False,
        "hasSword": False,
        "axeBonus": (5, 10),
        "swordBonus": (10,15),
        "hasTorch": False
    }
    
    SphinxRoom(player)