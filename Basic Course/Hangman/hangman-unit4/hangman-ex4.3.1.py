def main():
    guess = input("Guess a letter:")
    guess = guess.lower()
    # Check for non English letter and more than one letter
    if len(guess) > 1 and not guess.isalpha():
        print("E3")

    # Check for non English letter
    elif not guess.isalpha():
        print("E2")

    # Check for more than one letter
    elif len(guess) > 1:
        print("E1")

    # Valid character
    else:
        print(guess)


if __name__ == '__main__':
    main()
