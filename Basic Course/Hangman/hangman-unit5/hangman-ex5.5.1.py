def is_valid_input(letter_guessed):
    guess = letter_guessed.lower()
    # Check for more than one letter
    if len(guess) > 1:
        return False

    # Check for non English letter
    elif not guess.isalpha():
        return False

    # Valid character
    else:
        return True


def main():
    print(is_valid_input("A"))


if __name__ == '__main__':
    main()
