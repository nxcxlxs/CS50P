dict = {}
while True:
    try:
        # item = input().upper()
        # if item in dict:
            # dict[item] += 1
        # else:
            # dict[item] = 1
        key = input().upper()
        value = dict.get(key, 0)
        dict[key] = value + 1
    except (EOFError, KeyError):
        # for key in sorted(dict.keys()):
            # print(dict[key], key)
        # break
        print()
        for grocery, number in sorted(dict.items()):
            print(number, grocery)
        break


