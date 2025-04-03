def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False
    x = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not x:
                if char == "0":
                    return False
                x = True
            elif not s[i:].isdigit():
                return False
    return True



main()
