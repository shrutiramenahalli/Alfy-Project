import rock_paper_scissors_helper as helper

while (True):
    player = input("Enter your choice (machine, user) : ")
    if(player != "machine") & (player !="user"):
        print("You have entered incorrect option! Please chose from the options!")
        player = input("Enter your choice (machine, user) : ")
    else:
        helper.RPS_Game(player)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() == "y":
        player = input("Enter your choice (machine, user) : ")
        helper.RPS_Game(player)
    else:
        print("Thanks for playing!")
