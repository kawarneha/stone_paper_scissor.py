import random

print("how many times u wanna play this game....?")

x=int(input())

for i in range(x):

    comp=("scissor","stone","paper")

    choice=random.choice(comp)

    print("welcome:)")

    print("enter your choice for the game-----stone,paper,scissor")

    choice_u=input()

    print("computer choice - ",end="")

    print(choice,end="")

    print(" therfore ",end="")

    if(choice==choice_u):

        print("match is draw")

    elif(choice=="stone" and choice_u=="paper"):

        print("you won:)")

    elif(choice=="stone" and choice_u=="scissor"):

        print("you lose;(")

    elif(choice=="paper" and choice_u=="scissor"):
 
        print("you won:)")

    elif(choice=="paper" and choice_u=="stone"):

        print("u lose;(")

    elif(choice=="scissor" and choice_u=="stone"):

        print("u won:)")

    elif(choice=="scissor" and choice_u=="paper"):

        print("u lose;(")

    print("thanks for playing:]")