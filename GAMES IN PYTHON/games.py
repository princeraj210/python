# rock paper seasor ------------------------------------GAME 1
import random

while True:
    print("~~~~~~~~~ROCK PAPER SEASOR~~~~~~~~~~~~")
    user_score = 0
    bot_score = 0
    ties = 0
    name = input("enter your name here :")
    print("""
    winning rules ----
    1. paper vs rock --> paper
    2. rock vs scissors --> rock
    3. paper vs scissors --> scissors""")
    print()
    print("""
    choices are :
    1. rock
    2. paper
    3. scissor""")
    print()
    choice = int(input("enter your choice from 1-3 :"))
    while choice > 3 or choice < 1:
        choice = int(input("enter the valid choice:"))
    if choice == 1:
        user_choice = "rock"
    elif choice == 2:
        user_choice = "paper"
    else:
        user_choice = "scissors"

    print("the user choice is :", user_choice)
    print("now its computer turns")
    computer = random.randint(1, 3)

    if computer == 1:
        bot_choice = "rock"
    elif computer == 2:
        bot_choice = "paper"
    else:
        bot_choice = "scissors"

    print("computer choice is :", bot_choice)

    if (user_choice == "paper" and bot_choice == "rock") or (user_choice == "rock" and bot_choice == "paper"):
        print("paper wins")
        result = "paper"
    elif (user_choice == "scissors" and bot_choice == "rock") or (user_choice == "rock" and bot_choice == "scissors"):
        print("rock wins")
        print()
        result = "rock"
    elif (user_choice == bot_choice):
        print("it's a tie")
        print()
        result = "tie"
    else:
        print("scissors wins")
        print()
        result = "scissors"

    if result == "tie":
        ties += 1
    elif result == user_choice:
        print(name, "wins")
        user_score += 1
    else:
        print("computer wins")
        bot_score += 1

    print("scores are:")
    print(name, "'s score is :", user_score)
    print("computer's score is :", bot_score)
    print("ties are :", ties)

    repeat = input("do you want to play again ?")
    if repeat == "no" or repeat == "No":
        break
print("game over ! ")
print("thanks for playing ............")


# Anagram Game -----------------------------------------------------------GAME 2

words = ["ironman", "thor", "hawkeye", "wanda", "vision"]
word = random.choice(words)
jumble = "".join(random.sample(word, len(word)))
# print(jumble)
chances = 3
print("~"*30)
print("~~~~~~ Avengers Jumble Bumble ~~~~~~")
print()
while chances != 0:
    print("the word is :", jumble)
    guess = input("enter your guess words:").lower()
    if guess == word:
        print("correct guess !!")
        print("you won :)")
        break
    else:
        chances -= 1
        print("incorrect guess !!")
        print("remaining chances are :", chances)
else:
    print("all your chances are exhausted")
    print("you looose :(")
    print("the correct word is :", word)
print("thankyou for playung ------------")
