def show_hidden_word(secret_word, old_letters_guessed):
    hidden_word = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            hidden_word += letter + ' '
        else:
            hidden_word += '_ '
    return hidden_word


def main():
    secret_word = "spkvs"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))


if __name__ == '__main__':
    main()
