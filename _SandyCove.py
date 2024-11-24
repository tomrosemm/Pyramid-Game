# hasTorch = False#Test Variable
# hasAxe = False#Test Variable


def SandyCove():
    
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
    
    directions = ["FORWARD", "BACKWARD"]
    
    print("YOU ARE IN A SANDY COVE")
    
    if player["hasTorch"] == False:
        print("HINT TO TORCH")
        
    if player["hasAxe"] == False:
        print("HINT TO AXE")
        
    if player["hasTorch"] and player["hasAxe"]:
        print("TAKE ANOTHER SHOT AT THE RIDDLE")
        #UNLOCK RIDDLE SOMEHOW
    
    #Check health, refill if under full, say something if full
    
    print("YOU CAN TRAVEL FORWARD OR BACKWARDS")
    print("WHERE DO YOU WANT TO MOVE?")
    
    userInput = ''
    
    while userInput not in directions:
        print("CHOICES: FORWARD, BACKWARD")
        print("WHERE DO YOU WANT TO MOVE?")
        userInput = input().strip().upper()
        
        if userInput == "FORWARD":
            print("FORWARD: TO ROYAL TOMB")
            #RoyalTomb()
        
        elif userInput == "BACKWARD":
            print("BACKWARD: TO INNER BURIAL CHAMBER")
            #InnerBurialChamber()
        
        else:
            print("Please enter a valid direction.")
            