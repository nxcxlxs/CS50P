import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"src=\"https?://(?:www\.)?youtube\.com/embed/(\w+)\"", s, re.IGNORECASE):
        return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()
