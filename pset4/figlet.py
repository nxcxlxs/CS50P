import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
font_list = figlet.getFonts()

try:
    if len(sys.argv) == 2 or len(sys.argv) > 3:
        sys.exit("Invalid usage")

    elif sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in font_list:
        sys.exit("Invalid usage")

    else:
        plain = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print("Output:")
        print(figlet.renderText(plain))

except IndexError:
    plain = input("Input: ")
    random_font = random.choice(font_list)
    figlet.setFont(font=random_font)
    print("Output:")
    print(figlet.renderText(plain))