def LBCBattle():
        
    print("BATTLE LOGIC")

    #Meat of the fight logic
    
    global wonLBCBattle
    


def LesserBurialChamber():
    
    directions = ["RIGHT", "BACKWARD"]
    
    hasAxe = True#Test variable, will be influenced by picking up axe in encampment room
    hasSword = True#Test variable, will be influenced by getting sword in armory
    
    global wonLBCBattle
    
    print("YOU ARE IN THE INNER BURIAL CHAMBER")
    
    print("YOU ARE ATTACKED BY 2 TOMB GOBLINS AND A MUMMY")
    
    if hasSword:
        print("YOU HAVE A HOOKED SWORD")
        
    elif hasAxe and not hasSword:
        print("YOU HAVE AN AXE")
    
    else:
        print("STRAP IN")
    
    print("BEGIN BATTLE")
    
    LBCBattle()#Calls the LBCBattle function
    
    if wonLBCBattle:
        print("SUCCESSFUL BATTLE")
        print("YOU CAN TRAVEL RIGHT OR BACKWARD")
        print("WHERE DO YOU WANT TO MOVE?")
        userInput = ''
        
        while userInput not in directions:
            print("CHOICES: RIGHT, BACKWARD")
            userInput = input().upper()
            
            if userInput == "RIGHT":
                print("RIGHT: TO SPHINX ROOM")#Test print
                #SphinxRoom()
            
            elif userInput == "BACKWARD":
                print("BACKWARD: TO SNAKEWAY")
                #Snakeway()

            else:
                print("Please enter a valid direction.")

    else:
        print("YOU DIED!")
        quit()