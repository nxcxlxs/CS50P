import inflect

list = []
p = inflect.engine()

while True:
    try:
        names = input("Name: ")
        list.append(names)
        new_list = p.join(list, final_sep=",")

    except EOFError:
        print(f"Adieu, adieu, to {new_list}")
        break
