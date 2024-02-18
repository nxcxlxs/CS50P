def main():
    emoticon = input()
    print(convert(emoticon))


def convert(emoticon):
    emoji = (emoticon.replace(":)", "🙂")
                     .replace(":(", "🙁"))
    return emoji

main()
