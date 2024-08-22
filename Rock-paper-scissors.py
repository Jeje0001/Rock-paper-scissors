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

    if userinputs == goal:
        print(goal)
        print("you won")

    else:
        print(goal)

        print("You lost")


print(goal)

print("The game is over")

# continue at 46:40