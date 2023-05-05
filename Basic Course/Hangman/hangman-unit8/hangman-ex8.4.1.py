HANGMAN_PHOTOS = {1: "x-------x", 2: "\nx-------x\n|\n|\n|\n|\n|",
                  3: "\n    x-------x\n    |       |\n    |       0\n    |\n    |\n    |",
                  4: "\n    x-------x\n    |       |\n    |       0\n    |       |\n    |\n    |"
    , 5: "\n    x-------x\n    |       |\n    |       0\n    |      /|\ \n    |      /\n    |"
    , 6: "\n    x-------x\n    |       |\n    |       0\n    |      /|\ \n    |      / \ \n    |"}


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])


def main():
    print_hangman(6)


if __name__ == '__main__':
    main()
