dct = {}

while True:
    try:
        item = input()
        item = item.strip().lower()
        if item:
            dct[item] = dct.get(item, 0) + 1
    except EOFError:
        print("\n")
        break

for item in sorted(dct):
    print(f"{dct[item]} {item.upper()}")
