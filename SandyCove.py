from RoyalTomb import *

def SandyCove(player, roomStates):
    
    directions = ["FORWARD", "BACKWARD", "Q"]
    
    #Initialize the room states if not already done
    if "SandyCove" not in roomStates:
        roomStates["SandyCove"] = {"visited": False, "gryphonEventOccurred": False}
        
    if not roomStates["SandyCove"]["visited"]:
        print("WELCOME TO THE SANDY COVE FOR THE FIRST TIME")
        roomStates["SandyCove"]["visited"] = True
    
    else:
        print("WELCOME BACK TO THE SANDY COVE")
    
    print("YOU ARE IN A SANDY COVE")
    
    if not roomStates["SandyCove"]["gryphonEventOccurred"]:
        roomStates["SandyCove"]["gryphonEventOccurred"] = True
        
        if player["hasTorch"] == False:
            print("HINT TO TORCH")
            
        if player["hasAxe"] == False:
            print("HINT TO AXE")
            
        if player["hasTorch"] and player["hasAxe"]:
            print("TAKE ANOTHER SHOT AT THE RIDDLE")
            
            roomStates["SphinxRoom"]["riddleSolved"] = False
            roomStates["SphinxRoom"]["riddleFailed"] = False
        
        #Check health, refill if under full, say something if full
        if player["health"] < 100:
            print("LET'S HEAL YOU UP")
            player["health"] = 100
        
        else:
            print("WOW, HOW DID YOU MANAGE TO SURVIVE ALL THAT?")
            
    
    else:
        print("THE GRYPHON LOOKS AT YOU AS YOU ENTER. HE IS UNBOTHERED.")
    
    print("YOU CAN TRAVEL FORWARD OR BACKWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    
    userInput = ''
    
    while userInput not in directions:
        print("CHOICES: FORWARD, BACKWARD")
        print("Q TO QUIT")
        userInput = input().strip().upper()
        
        if userInput == "FORWARD":
            print("FORWARD: TO ROYAL TOMB")
            RoyalTomb(player, roomStates)
        
        elif userInput == "BACKWARD":
            from InnerBurialChamber import InnerBurialChamber
            print("BACKWARD: TO INNER BURIAL CHAMBER")
            InnerBurialChamber(player, roomStates)
            
        elif userInput == "Q":
<<<<<<< Updated upstream
            print("GOODBYE")
=======
            print("Goodbye.")
>>>>>>> Stashed changes
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
    
    SandyCove(player, roomStates)