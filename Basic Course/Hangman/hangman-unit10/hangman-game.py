# prints list of letters sorted with ->
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


# check if the letter is valid
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


# this func tries to update the list
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        print_sorted_letters(old_letters_guessed)
        return False


#  func prints the hangman state
def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {1: "x-------x", 2: "\nx-------x\n|\n|\n|\n|\n|",
                      3: "\n    x-------x\n    |       |\n    |       0\n    |\n    |\n    |",
                      4: "\n    x-------x\n    |       |\n    |       0\n    |       |\n    |\n    |"
        , 5: "\n    x-------x\n    |       |\n    |       0\n    |      /|\ \n    |      /\n    |"
        , 6: "\n    x-------x\n    |       |\n    |       0\n    |      /|\ \n    |      / \ \n    |"}
    print(HANGMAN_PHOTOS[num_of_tries])


# this func prints the opening for the game
def print_opening():
    print("Welcome to the game Hangman")
    print(""" 
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/ 
                                                               """)


# shows number of lines according to the hidden word
def show_hidden_word(secret_word, old_letters_guessed):
    hidden_word = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            hidden_word += letter + ' '
        else:
            hidden_word += '_ '
    return hidden_word

# check if the user won
def check_win(secret_word, old_letters_guessed):
    counter = 0
    for char in old_letters_guessed:
        if char in secret_word.lower():
            counter += 1
        if counter == len(secret_word):
            return True
    return counter == len(secret_word)


# choose the file path and index of the word
def choose_word(file_path, index):
    with open(file_path, 'r') as f:
        words = f.read().split()
    num_words = len(set(words))
    index = (index - 1) % len(words)
    secret_word = words[index]
    return secret_word

# game main loop
def game_loop():
    MAX_TRIES = 6
    num_of_tries = 1
    old_letters_guessed = []
    print_opening()
    while True:
        file_path = input("Enter file path:")
        index = int(input("Enter index:"))
        try:
            secret_word = choose_word(file_path, index)
            break
        except Exception as e:
            print("invalid file_path or index")
    print("Let’s start!")
    while num_of_tries < MAX_TRIES:
        print_hangman(num_of_tries)
        print(show_hidden_word(secret_word, old_letters_guessed))
        while True:
            guess = input("Guess a letter:")
            if try_update_letter_guessed(guess, old_letters_guessed):
                if guess not in secret_word:
                    print("):")
                break
        if check_win(secret_word, old_letters_guessed):
            print(show_hidden_word(secret_word, old_letters_guessed))
            print("WIN")
            break
        num_of_tries += 1
    if num_of_tries == MAX_TRIES:
        print_hangman(num_of_tries)
        print("LOSE")


def main():
    game_loop()


if __name__ == '__main__':
    main()
