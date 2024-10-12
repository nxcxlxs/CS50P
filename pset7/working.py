import re


# hour_dict = {1 : 13, 2 : 14, 3 : 15, 4 : 16, 5 : 17, 6 : 18, 7 : 19, 8 : 20, 9 : 21, 10 : 22, 11 : 23, 12 : 0}

pm_dict = {
    1 : 13, 2 : 14, 3 : 15, 4 : 16, 5 : 17, 6 : 18,
    7 : 19, 8 : 20, 9 : 21, 10 : 22, 11 : 23, 12 : 12
}

am_dict = {
    12: 0
}

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(1[0-2]|0?[1-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|0?[1-9]):?([0-5][0-9])? (AM|PM)$", s):

        start_hour = int(matches.group(1))
        start_min = matches.group(2) if matches.group(2) else "00"
        start_period = matches.group(3)

        end_hour = int(matches.group(4))
        end_min = matches.group(5) if matches.group(5) else "00"
        end_period = matches.group(6)

        # start_hour = hour_conversion[start_hour] if start_period == "PM" else start_hour
        # end_hour = hour_conversion[end_hour] if end_period == "PM" else end_hour

        if start_period == "PM" and start_hour in pm_dict:
            start_hour = pm_dict[start_hour]
        elif start_period == "AM" and start_hour in am_dict:
            start_hour = am_dict[start_hour]

        if end_period == "PM" and end_hour in pm_dict:
            end_hour = pm_dict[end_hour]
        elif end_period == "AM" and end_hour in am_dict:
            end_hour = am_dict[end_hour]

    else: raise ValueError

    return f"{start_hour:02}:{start_min} to {end_hour:02}:{end_min}"


if __name__ == "__main__":
    main()
