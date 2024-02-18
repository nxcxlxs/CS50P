def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s.isalpha():
        if 2 <= len(s) <= 6:
            return True
    if not any(s[i].isnumeric() and s[i + 1].isalpha() for i in range(len(s) - 1)):
        if s[0:2].isalpha():
            if 2 <= len(s) <= 6:
                if not any(char in s for char in [".", ",", "-", " "]):
                    for n in s:
                        if n.isnumeric():
                            number = n
                            break
                    if number is not None and number != "0":
                        return True
    return False

main()

# apparently it can be easier to check all the false assumptions first and then ask to return what is true.

# def is_valid(s):
    # if len(s) < 2 or len(s) > 6:
        # return False
    # if s[0:2].isalpha() == False:
        # return False
    # if any(s[i].isnumeric() and s[i+1].isalpha() for i in range(len(s) - 1)):
        # return False
    # i = 0
    # while i < len(s):
        # if s[i].isalpha() == False:
            # if s[i] == "0":
                # return False
            # else:
                # break
        # i += 1
    # for char in s:
        # if char in [".", ",", ";", ":", " ", "!", "?", "-"]:
            # return False
    # return True

# main()
