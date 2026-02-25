 #GUESS THE NUMBER 

import random
n = random.randint(1,6)
a = 1
guess = 0

while(guess <= 4 or a!=n):
    a = int(input("guess the num: "))
    if (a > n):
        print("guess the lower num ")
    elif(a < n):
        print("guess the higher num")
    else :
        print("match")    
    guess += 1

print(f"you guess thee currect num {n}\n and your attempts is {guess}")