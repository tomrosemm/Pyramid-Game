def SnakeWay():
    
    directions = ["forward", "backward"]
    
    hasTorch = True #Test variable, in execution will be linked to the action of taking torch in entrance
    
    print("YOU ARE IN THE SNAKEWAY")
    
    if hasTorch == False:
        print("YOU DON'T HAVE A LIGHT SOURCE, AND IT'S PITCH BLACK. YOU HEAR HISSING")
            
    else:
        print("YOU HAVE A HANDY DANDY TORCH")
    
    print("YOU CAN TRAVEL FORWARD OR BACKWARD")
    print("WHERE DO YOU WANT TO MOVE?")
    userInput = ''
    
    while userInput not in directions:
        print("CHOICE(S): FORWARD, BACKWARD")
        userInput = input()

        if userInput == "forward":   
            print("FORWARD: TO SPHINX ROOM") #Test Print
            
            if hasTorch == True:
                print("THE LIGHT OF THE TORCH ALLOWS YOU TO COMPLETELY AVOID THE SNAKES")
            
            else:
                print("YOU STUMBLE THROUGH THE DARKNESS AND INTO MORE THAN A COUPLE SNAKES. THEY BITE.")
                #Take damage
            
            #SphinxRoom()
            
        else:
            print("Please enter a valid direction.")
    