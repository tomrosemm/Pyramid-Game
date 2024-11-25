hasTorch = True #Test Variable
hasAxe = True #Test Variable

def Encampment():
    
    directions = ['forward', 'backward']
    print("YOU ARE IN THE ENCAMPMENT")   

    axeChoice = input("TAKE AXE? (y/n)").upper()
        
    if axeChoice == "Y":        
        hasAxe = True

    else:
        hasAxe = False
        print("NO AXE")

    EncampmentBattle() #Call the EncampmentBattle function

    print("YOU CAN TRAVEL FORWARD OR BACKWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
    
    while userInput not in directions:        
        print("CHOICE(S): FORWARD, BACKWARD")
        userInput = input().lower()

        if userInput == "forward":   
            print("FORWARD: TO SNAKEWAY") #Test Print
        elif userInput == "backward":
            print("BACKWARD TO ENTRANCE") #Test Print
            
def EncampmentBattle():
        
    print("BATTLE LOGIC")

    #Meat of the fight logic
    
    global wonEncampmentBattle