# import string

def main():
    var = input("camelCase: ")
    replacements = {
        "A": "_a", "B": "_b", "C": "_c",
        "D": "_d", "E": "_e", "F": "_f",
        "G": "_g", "H": "_h", "I": "_i",
        "J": "_j", "K": "_k", "L": "_l",
        "M": "_m", "N": "_n", "O": "_o",
        "P": "_p", "Q": "_q", "R": "_r",
        "S": "_s", "T": "_t", "U": "_u",
        "V": "_v", "W": "_w", "X": "_x",
        "Y": "_y", "Z": "_z"
}

    # replacements = {char: f"_{char.lower()}" for char in string.ascii_uppercase}

    result = convert(var, replacements)
    print("snake_case:", result)

def convert(var, replacements):
    for old, new in replacements.items():
        var = var.replace(old, new)

    return var


main()

# word = input("camelCase: ")

# print("snake_case: ", end="")

# for letter in word:
    # if letter.isupper():
        # print("_" + letter.lower(), end="")
    # else:
        # print(letter, end="")
# print()
