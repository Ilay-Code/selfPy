def check_valid_input(letter_guessed, old_letters_guessed):
    guess = letter_guessed.lower()
    # Check for more than one letter
    if len(guess) > 1:
        return False

    # Check for non English letter
    elif not guess.isalpha():
        return False
    elif guess in old_letters_guessed:
        return False
    # Valid character
    else:
        return True


def main():
    old_letters = ['a', 'b', 'c']

    print(check_valid_input('&', old_letters))


if __name__ == '__main__':
    main()
