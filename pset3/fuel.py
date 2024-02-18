while True:
    try:
        vol = input("Fraction: ")
        x, y = vol.split("/")
        if int(x) > int(y):
            continue # this keyword keeps the loop going, and prompting the user, if the condition is True.
        new_vol = round((int(x) / int(y)*100))
        if new_vol >= 99:
            print("F")
        elif new_vol <= 1:
            print("E")
        else:
            print(f"{new_vol}%")

        break

    except (ValueError, ZeroDivisionError):
        pass

# Dors Code School take on it.
# while True:
    # fuel = input("Fraction :")
    # try:
        # numerator, denominator = fuel.split("/")
        # new_numerator = int(numerator)
        # new_denominator = int(denominator)
        # f = new_numerator / new_denominator
        # if f <= 1:
            # break
    # except (ValueError, ZeroDivisionError):
        # pass
# p = int(f * 100)
# if p >= 99:
    # print("F")
# elif p <= 1:
    # print("E")
# else:
    # print(f"{p}%")
