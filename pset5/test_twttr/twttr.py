def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u",
              "A", "E", "I", "O", "U"]
    for char in vowels:
        word = word.replace(char, "")
    return word

# Optimized by ChatGPT:
# def shorten(word):
    # vowels = "aeiouAEIOU"
    # return ''.join(char for char in word if char not in vowels)

# Another method:
# def shorten(word):
    # list = []
    # for letter in word:
        # if letter.lower() not in ["a", "e", "i", "o", "u"]:
            # list.append(letter)
            # new_word = "".join(list)
    # return new_word

# Dors Coding School take on it:
# def shorten(word):
    # vowelless = ""
    # for letter in word:
        # if letter.lower() not in ["a", "e", "i", "o", "u"]:
            # vowelless += letter
    # return vowelless

if __name__ == "__main__":
    main()
