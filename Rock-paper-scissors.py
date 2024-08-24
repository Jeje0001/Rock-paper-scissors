import random

userscore=0
computer=0
goal=None
while True:
    userinputs=input("Enter either rock,paper,scissors or  Enter q to exit: ").lower()

    if userinputs == "q":
        break
    if userinputs not in ["rock","paper","scissors"]:
        continue
    array=["rock","paper","scissors"]

    r=random.randrange(0,3)
    goal=array[r]

    if userinputs == "rock" and goal  == "scissors":
        print(goal)
        print("you won")
        userscore+=1
    elif userinputs == "paper" and goal == "rock":
        print(goal)
        print("you won")
        userscore+=1
    elif userinputs == "scissors" and goal == "paper":
        print(goal)
        print("you won")
        userscore+=1
    elif userinputs == goal:
        print("it is a draw")        
    
    else:
        print(goal)
        print("you lost")
        computer+=1



print("computer won " + str(computer) + " times")
            
print("You won " + str(userscore) + " times")

# print(goal)

# print("The game is over")

# continue at 46:40