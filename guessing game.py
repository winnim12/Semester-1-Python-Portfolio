#Winni Ma
#11/11/24

#Init
import random

#Function
def generator():
    ans = input("Choose a difficulty level; Easy (E), Medium (M), or Hard (H)?")
    if ans == 'E':
        print("Guess the number to win the game.")
        guess = int(input("Guess the number."))
        number = random.randint(0,10)
        if number == guess:
            print("Congratulations, You win!")
        else:
            if number > guess:
                print("Guess is too low")
            if number < guess:
                print("Guess is too high")
            print("You have 2 more guesses. Try again.")
            guess = int(input("Guess the number."))
            if number == guess:
                print("Congratulations, You win!")
            else:
                if number > guess:
                    print("Guess is too low")
                if number < guess:
                    print("Guess is too high")
                print("You have 1 more guess. Try again.")
                guess = int(input("Guess the number."))
                if number == guess:
                    print("Congratulations, You win!")
                else:
                    print("You lost. The number was..")
                    print(int(number))
    if ans == 'M':
        print("Guess the number to win the game.")
        guess = int(input("Guess the number."))
        number = random.randint(0,20)
        if number == guess:
            print("Congratulations, You win!")
        else:
            if number > guess:
                print("Guess is too low")
            if number < guess:
                print("Guess is too high")
            print("You have 2 more guesses. Try again.")
            guess = int(input("Guess the number."))
            if number == guess:
                print("Congratulations, You win!")
            else:
                if number > guess:
                    print("Guess is too low")
                if number < guess:
                    print("Guess is too high")
                print("You have 1 more guess. Try again.")
                guess = int(input("Guess the number."))
                if number == guess:
                    print("Congratulations, You win!")
                else:
                    print("You lost. The number was..")
                    print(int(number))

    if ans == 'H':
        print("Guess the number to win the game.")
        guess = int(input("Guess the number."))
        number = random.randint(0,30)
        if number == guess:
            print("Congratulations, You win!")
        else:
            if number > guess:
                print("Guess is too low")
            if number < guess:
                print("Guess is too high")
            print("You have 2 more guesses. Try again.")
            guess = int(input("Guess the number."))
            if number == guess:
                print("Congratulations, You win!")
            else:
                if number > guess:
                    print("Guess is too low")
                if number < guess:
                    print("Guess is too high")
                print("You have 1 more guess. Try again.")
                guess = int(input("Guess the number."))
                if number == guess:
                    print("Congratulations, You win!")
                else:
                    print("You lost. The number was..")
                    print(int(number))


#Main
generator()
