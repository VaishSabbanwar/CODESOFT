print("MY CALSI")

num1=float(input("Enter the number 1:-"))
num2=float(input("Enter the number 2:-"))

print("press 1 for add \npress 2 for subtract \npress 3 for multiply \npress 4 for divide")

choice= int(input("Enter the choice:--"))
if choice ==1:
    print ("THE ADDITION OF TWO NUMBERS>>",num1+num2)
elif choice == 2:
    print ("THE SUBTRACTION OF TWO NUMBERS>>",num1-num2)
elif choice == 3:
    print ("THE MULTIPLICATION OF TWO NUMBERS>>",num1*num2)
elif choice == 4:
    print ("THE DIVISION OF TWO NUMBERS>>",num1/num2)
else:
    print("Invalid Input") 