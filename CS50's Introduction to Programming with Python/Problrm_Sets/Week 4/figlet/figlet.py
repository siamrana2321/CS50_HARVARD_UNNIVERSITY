import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        font = "standard"
    elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font'] and sys.argv[2] in fonts:
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")

    figlet.setFont(font=font)
    text = input("Input: ")
    print("Output:")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
