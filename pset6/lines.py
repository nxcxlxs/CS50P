import sys


if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

else:
    try:
        line_count = 0
        with open(sys.argv[1]) as f:
            for line in f:
                clean_line = line.strip()
                if clean_line and not clean_line.startswith("#"):
                    # Having trouble wrapping my mind around this condition checking.
                    # Apparently 'if clean_line' means the same as 'if clean_line != ""'...
                    line_count += 1
        print(line_count)

    except FileNotFoundError:
        sys.exit("File does not exist")
