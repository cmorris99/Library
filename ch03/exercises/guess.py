import random

def main():
    print("GUESS A NUMBER ONE THRU 100")
    print("YOU HAVE 3 ATTEMPTS")
    print("--------------")

    numb = random.randint(1, 10)
    guesses = 0

    while guesses < 3:
        guess = int(input("ENTER YOUR GUESS: "))
        guesses += 1

        if guess > numb:
            print("TOO HIGH TRY AGAIN!")

        elif guess < numb:
            print("TOO LOW TRY AGAIN!")

        else:
            print("YOU WON!!!")
            print(f"IT TOOK YOU {guesses} TRIES")
            return

    print("YOU DIDN'T GET IT.")
    print(f"THE NUMBER WAS {numb}")

main()