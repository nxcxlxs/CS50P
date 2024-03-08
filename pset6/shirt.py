import sys, os
from PIL import Image, ImageOps
# wget https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png
# wget https://cs50.harvard.edu/python/2022/psets/6/shirt/muppets.zip
# unzip muppets.zip

suffixes = [".jpg", ".jpeg", ".png"]

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

arg1 = sys.argv[1].lower()
arg2 = sys.argv[2].lower()

if not any(arg.endswith(tuple(suffixes)) for arg in (arg1, arg2)):
    sys.exit("Invalid input")

# suffix1 = arg1[arg1.rfind("."):]
# suffix2 = arg2[arg2.rfind("."):]
name1, suffix1 = os.path.splitext(arg1)
name2, suffix2 = os.path.splitext(arg2)

if not suffix1 == suffix2:
    sys.exit("Input and output have different extensions")
else:
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        before = Image.open(sys.argv[1])
        after = ImageOps.fit(before, size)

        after.paste(shirt, shirt)
        after.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")
