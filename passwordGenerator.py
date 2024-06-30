import random
import string

print("Welcome To Our PASSWORD_GENERATOR>> ")

def function():
    length= int(input("Enter the lenght of PASSWORD:>"))
    lowerD=string.ascii_lowercase
    upperD=string.ascii_uppercase
    digitD=string.digits
    symbolD=string.punctuation
    combine=lowerD+upperD+digitD+symbolD
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
    function()
function()
