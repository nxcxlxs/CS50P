import random


def main():
    count = 0
    score = 0
    wrong = 0
    lvl = get_level()

    while count < 10:
        try:
            x, y = generate_integer(lvl), generate_integer(lvl)
            answer = input(f"{x} + {y} = ")
            if answer.isnumeric() and int(answer) == int(x + y):
                count += 1
                score += 1
            else:
                while wrong < 2:
                    print("EEE")
                    wrong += 1
                    try:
                        answer = int(input(f"{x} + {y} = "))
                        if answer == int(x + y):
                            break
                    except ValueError:
                        pass
                else:
                    print("EEE")
                    print(f"{x} + {y} = {x + y}")
                    count += 1

        except ValueError:
            pass

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            # Again, it was crucial to keep the variables under the scope of the functions that operate with it.
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
