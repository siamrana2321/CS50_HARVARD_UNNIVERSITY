t = True
while t:
    try:
        a = input("Fraction: ")
        b, c = a.split("/")
        d, f = float(b), float(c)
        x, y = int(b), int(c)

        if y == 0:
            raise ZeroDivisionError
            # break
        if (x<d) or (y<f):
            raise ValueError
            # break
        if (x > y):
            raise ValueError
            break

        percentage = round((x / y) * 100)

        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
        t = False
    except (ValueError, ZeroDivisionError):
        pass
