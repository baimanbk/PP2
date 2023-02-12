from random import randrange
# -------------------------------------
#13 task
def guess_the_number():
    gue=0
    name=str(input("Hello! What is your name?\n"))

    print("Well",name, ',',"I am thinking of a number between 1 and 20.")

    number=randrange(1,21)

    while True:
        print("Take a guess")
        guess=int(input())
        if number==guess:
            print("Good job, KBTU! You guessed my number",gue, "in guesses!")
            break
        elif guess<number:
            gue+=1
            print("Your guess is too low.")
        else:
            gue+=1
            print("Your guess is too high.")

# print(guess_the_number())