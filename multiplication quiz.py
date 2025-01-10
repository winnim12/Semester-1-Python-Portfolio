#Winni Ma
#01/08/25

import random


number = 1
score = 0

def quiz():
    print("Welcome to Multiplication quiz!")
    global number
    global score
    mode = input("Do you want to play regular (r) or infinite (i) mode?: ")
    if mode == "r":
        level = input("Choose a difficulty level. Easy (e), medium (m), or hard (h): ")
        if level == "e":
            for i in range(5):
                num1 = random.randint(1,5)
                num2 = random.randint(1,5)
                question = "what is " + str(num1) + " x " + str(num2) + " ?"
                answer = num1 * num2

                print("Question:")
                number = number + 1
                response = input("what is " + question + "?")
                if int(response) == answer:
                    print("Correct!")
                    print("The answer was: " + str(answer))
                    score = score + 1
                elif int(response) != answer:
                    print("Incorrect?")
                    print("The answer was " + str(answer))

        if level == "m":
            for i in range(5):
                num1 = random.randint(1,8)
                num2 = random.randint(1,8)
                question = "what is " + str(num1) + " x " + str(num2) + " ?"
                answer = num1 * num2


                print("Question:")
                number = number + 1
                response = input("what is " + question + "?")
                if int(response) == answer:
                    print("Correct!")
                    print("The answer was: " + str(answer))
                    score = score + 1
                elif int(response) != answer:
                    print("Incorrect?")
                    print("The answer was " + str(answer))

        if level == "h":
            for i in range(5):
                num1 = random.randint(5,10)
                num2 = random.randint(5,10)
                question = "what is " + str(num1) + " x " + str(num2) + " ?"
                answer = num1 * num2


                print("Question:")
                number = number + 1
                response = input("what is " + question + "?")
                if int(response) == answer:
                    print("Correct!")
                    print("The answer was: " + str(answer))
                    score = score + 1
                elif int(response) != answer:
                    print("Incorrect?")
                    print("The answer was " + str(answer))

    if mode == "i":
        while True:
            for i in range(5):
                num1 = random.randint(1,5)
                num2 = random.randint(1,5)
                question = "what is " + str(num1) + " x " + str(num2) + " ?"
                answer = num1 * num2

                print("Question:")
                number = number + 1
                response = input("what is " + question + "?")
                if int(response) == answer:
                    print("Correct!")
                    print("The answer was: " + str(answer))
                    score = score + 1
                elif int(response) != answer:
                    print("Incorrect?")
                    print("The answer was " + str(answer))


            play = input("Do you want to keep playing? Yes (y) or no (n): ")
            if play == "y":
                print("Continuing game...")
            if play == "n":
                break
            
        print("Your score is: " + str(score) + "/5.")

quiz()
