# The Snake,Water,Gun Game 
import random
'''
1 = Snake
-1 = Water
0 = Gun
'''
computer = random.choice ([1, -1, 0])

your = str(input(" Enter your choice: "))

youDict = {
    "s" : 1,
    "w" : -1,
    "g" : 0
}

you = youDict[your]

reversedDict = {
    1 : "Snake",
    -1 : "Water",
    0 : "Gun"
}

print(f" You chose {reversedDict[you]} \n Computer chose {reversedDict[computer]}")

if(computer == you):
    print(" Game Draw ")

elif(computer == 0 and you == -1 ):
    print(" You Lose! ")

elif(computer == 0 and you == 1 ):
    print(" You Win! ")

elif(computer == 1 and you == 0 ):
    print(" You Win! ")

elif(computer == 1 and you == -1 ):
    print(" You Lose! ")

elif(computer == -1 and you == 0 ):
    print(" You Win! ")

elif(computer == -1 and you == 1 ):
    print(" You Lose! ")
