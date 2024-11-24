def SphinxRoom():
    
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
    
    directions = ["BACKWARD", "RIGHT"] #Changes if riddle is solved, as door is open
    
    hasTorch = True #Test variable, in execution will be linked to the action of taking torch in entrance
    
    riddleAnswer = "THE ANSWER"
    
    print("YOU ARE IN THE ROOM OF THE SPHINX")
    
    print("A SPHINX GREETS YOU")
    
    if hasTorch:
        print("THE SPHINX SEEMS TO GREATLY ENJOY THE LIGHT OF THE TORCH")
    
    else:
        print("THE ROOM IS DIM AND MUSTY")
    
    print("THE SPHINX ASKS YOU A RIDDLE. THE ANSWER IS: THE ANSWER")
    playerRiddleAnswer = ''
    playerRiddleAnswer = input().upper()
    
    if riddleAnswer == playerRiddleAnswer:
        print("YOU WERE CORRECT")
        
        if hasTorch:
            print("SPHINX THANKS YOU FOR THE LIGHT TOO.")
            #Give torch reward
        
        print("SPHINX CRUMBLES TO REVEAL A DOOR")
        riddleSolved = True
        directions = ["forward", "backward", "right"]
    
    else:
        print("YOU WERE WRONG")
        
        if hasTorch:
            print("SPHINX THANKS YOU FOR THE LIGHT THOUGH")
            #Give torch reward
        
        riddleSolved = False
    
    print("YOU CAN TRAVEL " + ", ".join(directions))
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
    
    while userInput not in directions:
        print("CHOICES: " + ", ".join(directions).upper())
        userInput = input().upper
        
        if userInput == "FORWARD" & riddleSolved:
            print("YOU STEP OVER THE CRUMBLED SPHINX")
            print("FORWARD: TO ARMORY")#Test print
            #Armory()
        
        elif userInput == "FORWARD" & riddleSolved == False:
                print("THE SPHINX GROWLS AS YOU APPROACH")
                #If there's time can we do something where you can push it further and enter an unbeatable battle with the sphinx?
        
        elif userInput == "RIGHT":
            print("RIGHT: TO INNER BURIAL CHAMBER") #Test print
            #InnerBurialChamber()
        
        elif userInput == "BACKWARD":
            print("BACKWARD: TO SNAKEWAY")#Test print
            #Snakeway()
        
        else:
            print("Please enter a valid direction.")
            