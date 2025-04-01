def main():
    x = input("What time is it?")
    a = convert(x)
    if (a>=7 and a<=8):
        print("breakfast time")
    if (a>=12 and a<=13):
        print("lunch time")
    if (a>=18 and a<=19):
        print("dinner time")


def convert(time):
    h, m = map(float, time.split(":"))
    return h+(m/60)


if __name__ == "__main__":
    main()
