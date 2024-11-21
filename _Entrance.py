def Entrance():
    
    directions = ["forward"]    
    hasTorch = False
    
    print("YOU ARE IN THE ENTRANCE")   
    torchChoice = input("TAKE TORCH? (y/n)").upper()
    
    if torchChoice == "Y":        
        hasTorch = True
    
    else:     
        hasTorch = False
        print("NO TORCH")
    
    print("YOU CAN TRAVEL ONLY FORWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
    
    while userInput not in directions:        
        print("CHOICE(S): FORWARD")
        userInput = input().upper()

        if userInput == "FORWARD":   
            print("FORWARD: TO ENCAMPMENT") #Test Print
            
            if hasTorch:
                print("THE LIGHT OF THE TORCH GUIDES YOUR WAY")
            
            #Encampment()
            
        else:
            print("Please enter a valid direction.")
    