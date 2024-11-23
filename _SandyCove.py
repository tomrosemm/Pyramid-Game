hasTorch = False#Test Variable
hasAxe = False#Test Variable


def SandyCove():
    
    global hasTorch
    global hasAxe
    
    directions = ["FORWARD", "BACKWARD"]
    
    print("YOU ARE IN A SANDY COVE")
    
    if not hasTorch:
        print("HINT TO TORCH")
        
    if not hasAxe:
        print("HINT TO AXE")
        
    if hasTorch and hasAxe:
        print("TAKE ANOTHER SHOT AT THE RIDDLE")
        #UNLOCK RIDDLE SOMEHOW
    
    #Check health, refill if under full, say something if full
    
    print("YOU CAN TRAVEL FORWARD OR BACKWARDS")
    print("WHERE DO YOU WANT TO MOVE?")
    
    userInput = ''
    
    while userInput not in directions:
        print("CHOICES: FORWARD, BACKWARD")
        print("WHERE DO YOU WANT TO MOVE?")
        userInput = input().upper()
        
        if userInput == "FORWARD":
            print("FORWARD: TO ROYAL TOMB")
            #RoyalTomb()
        
        elif userInput == "BACKWARD":
            print("BACKWARD: TO INNER BURIAL CHAMBER")
            #InnerBurialChamber()
        
        else:
            print("Please enter a valid direction.")
            