import random

def get_positive_integer(prompt) :
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass

def main():
    level = get_positive_integer("Level: ")

    secret_number = random.randint(1, level)

    while True:
        guess = get_positive_integer("Guess: ")

        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
