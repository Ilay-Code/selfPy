def print_sorted_letters(letters):
    # sort the list
    letters.sort()
    # join the letters into a string separated by arrows
    arrow = ' -> '
    sorted_letters_str = arrow.join(letters)
    # convert the string to lowercase
    sorted_letters_str = sorted_letters_str.lower()
    # print the result
    print(sorted_letters_str)


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


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print_sorted_letters(old_letters_guessed)
        return False


def main():
    old_letters = ['a', 'p', 'c', 'f']
    try_update_letter_guessed('$', old_letters)


if __name__ == '__main__':
    main()
