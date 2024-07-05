import random

l=["rock","paper","scissor"]

'''
rock vs paper >>paper wins
rock vs scissor >>rock wins
paper vs scissor >>scissor wins
'''

while True:
    ccount=0
    ucount=0
    uc=int(input('''
     Game Start...
     1.Yes
     2.No|Exit       
            
            '''))
    if uc==1:
        for a in range(1,6):
            userInput= int(input('''
       1.Rock 
       2.Paper
       3.Scissor            
                     '''))
            if userInput==1:
                userchoice= "rock"
            elif userInput==2:
                userchoice= "paper"
            elif userInput==3:
                userchoice= "scissor"  
            compChoice=random.choice(l)
            print("COMPUTER VALUE",compChoice)
            print("USER VALUE",userchoice)
            if compChoice==userchoice:
                print("GAME DRAW")   
                ucount= ucount+1
                ccount= ccount+1
            elif (userchoice=="rock" and compChoice=="scissor") or (userchoice=="paper" and compChoice=="rock") or (userchoice=="scissor" and compChoice=="paper"):
                print("YOU WIN")
                ucount=ucount+1
            else:
                print("COMPUTER WIN")
                ccount= ccount+1
        print("FINAL SCORE - ")
        print("COMPUTER : ", ccount)
        print("USER : ", ucount)
    elif uc==2:
        break
    else:
        print("Invalid input. Please enter 1 or 2.")