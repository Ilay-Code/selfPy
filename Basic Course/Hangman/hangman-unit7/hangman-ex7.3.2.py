def check_win(secret_word, old_letters_guessed):
    counter = 0
    for char in old_letters_guessed:
        if char in secret_word:
            counter += 1
        if counter == len(secret_word):
            return True
    return counter == len(secret_word)


def main():
    secret_word = "yes"
    old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'v']
    print(check_win(secret_word, old_letters_guessed))


if __name__ == '__main__':
    main()
