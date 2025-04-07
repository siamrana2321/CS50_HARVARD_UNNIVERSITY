import inflect

p = inflect.engine()
names = []

try:
    while True:
        name = input("Name: ").strip()
        if name:
            names.append(name)
except EOFError:
    print()

msg = f"Adieu, adieu, to {p.join(names)}"
print(msg)
