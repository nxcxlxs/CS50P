def main():
    t = input("What time is it? ")
    time = convert(t)

    if 7.0 <= time <= 8.0:
        print("breakfast time")

    elif 12.0 <= time <= 13.0:
        print("lunch time")

    elif 18.0 <= time <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    float_minutes = float(minutes) / 60
    float_hours = float(hours)
    return float_hours + float_minutes

#it was decisive, to overcome the assignment errors, that all the operations with the time were made under the convert() scope.

if __name__ == "__main__":
    main()