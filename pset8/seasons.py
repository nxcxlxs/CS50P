from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    print(convert(input("Date of Birth: ")))


def convert(s):
    try:
        days = (date.today() - date.fromisoformat(s)).days
        minutes = days * 24 * 60
        return f"{p.number_to_words(minutes, andword ='').capitalize()} minutes"

    except ValueError:
        sys.exit("Invalid Date")


if __name__ == "__main__":
    main()
