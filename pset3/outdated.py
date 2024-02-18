months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            month, day, year = date.split(sep="/")

        elif "," in date:
            month, day, year = date.split(sep=" ")
            day = day.strip(",")
            month = month.title()
            if month in months_list:
                month = (int(months_list.index(month)) + 1)
        else:
            continue

        if int(day) <= 31 and int(month) <= 12:
            print(f"{year}-{int(month):02}-{int(day):02}")
            break

    except (ValueError, NameError):
        pass
