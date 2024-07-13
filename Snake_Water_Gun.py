import random as r


def check(comp, user):
    if comp == user:
        return 0
    if comp == 0 and user == 1:
        return -1
    if comp == 1 and user == 2:
        return -1
    if comp == 2 and user == 0:
        return -1
    return 1


print("\t\t\tWelcome to the Game")
print("Choices:\n0 - Snake\t1 - Water\t2 - Gun")
number_of_time = int(input("Enter Number of times you wanna play: "))
for i in range(number_of_time):
    computer = r.randint(0, 2)
    player = int(input("\nEnter Your Choice(0/1/2): "))

    score = check(computer, player)

    print("You: ", player)
    print("Computer: ", computer)

    if score == 0:
        print("Draw")
    elif score == 1:
        print("You Won")
    else:
        print("You Lose")

