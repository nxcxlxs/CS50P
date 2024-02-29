import sys
import csv


if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

else:
    try:
        with open(sys.argv[1], 'r') as t:
            reader = csv.DictReader(t)
            modified_data = []
            for row in reader:
                second, first = (row['name']).split(",")
                house = row['house']
                # Be aware of subtle errors, like white spaces before the first name...
                modified_data.append([first.strip(), second, house])

                with open(sys.argv[2], 'w') as nt:
                    writer = csv.writer(nt)
                    writer.writerow(['first', 'last', 'house'])
                    writer.writerows(modified_data)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
