word = input("Input: ")

print("Output: ", end="")

for letter in word:
    if letter.lower() not in ["a", "e", "i", "o", "u"]:
        print(letter, end="")

print()