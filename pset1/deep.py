qst = input("What is the Great Answer to the Great Question of Life, the Universe and Everything? ")

match qst.strip().lower():
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
