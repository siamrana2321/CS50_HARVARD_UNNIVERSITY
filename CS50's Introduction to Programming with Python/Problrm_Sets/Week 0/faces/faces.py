def convert(str) :
    return str.replace(":)","🙂").replace(":(","🙁")

def main():
    x = input()
    print(convert(x))
main()
