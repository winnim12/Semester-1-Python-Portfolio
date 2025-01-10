#Winni Ma
#1/6/25

import random

player_score = 0
computer_score = 0
tie_count = 0

def game():
    while True:
        print("Welcome to Rock, Paper, Scissors.")
        #Player
        player = input("Choose rock (rock), paper (paper), or scissors (scissors)?")

        #Computer
        comp = random.randint(1,3)
        if comp == 1:
            comp = "rock"
            print ("Computer chose rock.")
        elif comp == 2:
            comp = "paper"
            print ("Computer chose paper.")
        elif comp == 3:
            comp = "scissors"
            print ("Computer chose scissors.")


        global computer_score
        global player_score
        global tie_count

        if player == "rock" and comp == "paper":
            print("You lost.")
            computer_score = computer_score + 1
        elif player == "paper" and comp == "scissors":
            print("You lost.")
            computer_score = computer_score + 1
        elif player == "scissors" and comp == "rock":
            print("You lost.")
            computer_score = computer_score + 1


        elif player == "rock" and comp == "scissors":
            print("You won.")
            player_score = player_score + 1
        elif player == "paper" and comp == "rock":
            print("You won.")
            player_score = player_score + 1
        elif player == "scissors" and comp == "paper":
            print("You won.")
            player_score = player_score + 1
        else:
            print("Tie!")
            tie_count = tie_count + 1

        print("Your score is " + str(player_score))
        print("The computer's score is " + str(computer_score))
        print("There has been " + str(tie_count) + " ties.")

        play = input("Do you want to keep playing? Yes (y) or no (n)?")
        if play == "y":
            print("Restarting game.")
        elif play == "n":
            break

game()
