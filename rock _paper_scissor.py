import random 

# List of choices for the game
choices = ["rock", "paper", "scissor"]

while True:
    ccount = 0  # Counter for computer wins
    ucount = 0  # Counter for user wins
    
    # Prompting the user to start the game or exit
    uc = int(input('''
     Game Start...
     1. Yes
     2. No | Exit       
            
    '''))
    
    if uc == 1:
        # Loop for 5 rounds of the game
        for _ in range(5):
            userInput = int(input('''
            1. Rock 
            2. Paper
            3. Scissor            
            '''))
            
            # Mapping user input to choices
            if userInput == 1:
                userchoice = "rock"
            elif userInput == 2:
                userchoice = "paper"
            elif userInput == 3:
                userchoice = "scissor"
            else:
                print("Invalid input. Please enter a number from 1 to 3.")
                continue
                
            # Randomly selecting computer's choice
            compChoice = random.choice(choices)
            print("COMPUTER VALUE:", compChoice)
            print("USER VALUE:", userchoice)
            
            # Determining the result of the round
            if compChoice == userchoice:
                print("GAME DRAW")
                ucount += 1
                ccount += 1
            elif (userchoice == "rock" and compChoice == "scissor") or \
                 (userchoice == "paper" and compChoice == "rock") or \
                 (userchoice == "scissor" and compChoice == "paper"):
                print("YOU WIN")
                ucount += 1
            else:
                print("COMPUTER WINS")
                ccount += 1
        
        # Printing final scores after 5 rounds
        print("\nFINAL SCORE - ")
        print("COMPUTER:", ccount)
        print("USER:", ucount)
        
    elif uc == 2:
        # Exiting the game if user chooses to exit
        break
    else:
        # Handling invalid input
        print("Invalid input. Please enter 1 or 2.")
