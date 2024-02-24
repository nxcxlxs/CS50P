def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0:2].isalpha() == False:
        return False
    if any(s[i].isnumeric() and s[i+1].isalpha() for i in range(len(s) - 1)):
        return False
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i += 1
    for char in s:
        if char in [".", ",", ";", ":", " ", "!", "?", "-"]:
            return False
    return True


if __name__ == "__main__":
    main()
