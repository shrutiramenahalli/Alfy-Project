import random

def RPS_Game(player):
    you = 0
    player2 = 0
    possible_actions = ["r", "p", "s"]
    while (you != 3) and (player2 != 3):
        user1 = input("User1: Enter your Choice (" + ", ".join(possible_actions) + ") : ")
        if(user1 == "!"):
            exit(1)

        if(user1 not in possible_actions):
            print("Please choose from options!")
            continue

        if (player == "machine"):
            user2 = random.choice(possible_actions)
        else:
            user2 = input("User2: Enter your Choice (" + ", ".join(possible_actions) + ") : ")
            if (user2 == "!"):
                exit(1)

            if (user2 != "r") & (user2 != "p") & (user2 != "s"):
                print("Please choose from options!")
                user2 = input("Enter your Choice (" + ", ".join(possible_actions) + ") : ")

        if user1 == user2:
            print(f"Both players selected {user1}. It's a tie!")
        elif user1 == "r":
            if (user2) == "s":
                you += 1
                print(f"You: {you}, Player2: {player2}")
            else:
                player2 += 1
                print(f"You: {you}, Player2: {player2}")
        elif user1 == "p":
            if user2 == "r":
                you += 1
                print(f"You: {you}, Player2: {player2}")
            else:
                player2 += 1
                print(f"You: {you}, Player2: {player2}")
        elif user1 == "s":
            if user2 == "p":
                you += 1
                print(f"You: {you}, Player2: {player2}")
            else:
                player2 += 1
                print(f"You: {you}, Player2: {player2}")
    if (player2 > you):
        total = (you, player2)
        print("\n You Lost!!!! Better Luck Next Time \n")
    else:
        total = (you, player2)
        print("Congratulations!!!! You Won!...HURRAY!!!")
    print(f"Total Points : you = {you}, Player2 = {player2}")
    return total