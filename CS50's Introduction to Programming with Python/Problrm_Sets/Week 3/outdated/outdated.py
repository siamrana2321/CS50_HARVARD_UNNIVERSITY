months = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}

while True:
    try:
        date = input("Date: ").strip()

        if "/" in date:
            month, day, year = date.split("/")

        elif "," in date:
            month_str, day, year = date.replace(",", "").split()
            month = months.get(month_str)
            if month is None:
                raise ValueError
        else:
            raise ValueError

        month, day, year = int(month), int(day), int(year)

        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError

        print(f"{year:04d}-{month:02d}-{day:02d}")
        break
    except (ValueError, KeyError):
        pass
