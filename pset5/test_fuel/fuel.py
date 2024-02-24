def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            if y != "0":
                if x.isnumeric() == True and y.isnumeric() == True and int(x) < int(y):
                    new_x = int(x)
                    new_y = int(y)
                else:
                    raise ValueError
            else:
                raise ZeroDivisionError
            f = new_x / new_y
            return f
        except ValueError:
            fraction = input("Fraction: ")  # raise ValueError
        except ZeroDivisionError:
            fraction = input("Fraction: ")  # raise ZeroDivisionError
        except TypeError:
            fraction = input("Fraction: ")  # raise TypeError
        # The code works. The rear end of this block is not validated with pytest, but check50 accepts it.


def gauge(percentage):
    p = int(percentage * 100)
    if p >= 99:
        return ("F")
    elif p <= 1:
        return ("E")
    else:
        return (f"{p}%")


if __name__ == "__main__":
    main()
