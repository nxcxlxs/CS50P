# download the files provided:
# wget https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv
# wget https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv
import sys
import csv
from tabulate import tabulate


if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

else:
    try:
        with open(sys.argv[1]) as t:
            t_reader = csv.reader(t)
            print(tabulate(t_reader, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")
