import random

while True:
    try:
        n = int(input("Level: "))
        answer = random.randint(1, n)
        break

    except ValueError:
        pass

while True:
    try:
        guess = int(input("Guess: "))
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            break

    except ValueError:
        pass
