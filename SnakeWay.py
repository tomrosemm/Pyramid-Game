from SphinxRoom import *

def SnakeWay(player):
    
    # player = {
    # "name": "Player",
    # "health": 100,
    # "baseDamageRange": (10,20),
    # "hasAxe": False,
    # "hasSword": False,
    # "axeBonus": (5, 10),
    # "swordBonus": (10,15),
    # "hasTorch": False
    # }
    
    directions = ["FORWARD", "BACKWARD"]
    
    print("YOU ARE IN THE SNAKEWAY")
    
    if player["hasTorch"] == False:
        print("YOU DON'T HAVE A LIGHT SOURCE, AND IT'S PITCH BLACK. YOU HEAR HISSING")
            
    else:
        print("YOU HAVE A HANDY DANDY TORCH")
    
    print("YOU CAN TRAVEL FORWARD OR BACKWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
    
    while userInput not in directions:
        print("CHOICE(S): FORWARD, BACKWARD")
        userInput = input().strip().upper()

        if userInput == "FORWARD":   
            print("FORWARD: TO SPHINX ROOM") #Test Print
            
            if player["hasTorch"]:
                print("THE LIGHT OF THE TORCH ALLOWS YOU TO COMPLETELY AVOID THE SNAKES")
            
            else:
                print("YOU STUMBLE THROUGH THE DARKNESS AND INTO MORE THAN A COUPLE SNAKES. THEY BITE.")
                #Take damage
            
            SphinxRoom(player)
        
        elif userInput == "BACKWARD":
            print("BACKWARD: TO ENCAMPMENT")
            #Encampment()
            
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
    
    SnakeWay(player)
        