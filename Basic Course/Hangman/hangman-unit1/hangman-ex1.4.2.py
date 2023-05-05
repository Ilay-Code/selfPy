# this func gets num of stage prints the state of the hangman
def draw_hangman(num):
    if num == 1:
        print("x-------x")
    elif num == 2:
        print("\nx-------x\n|\n|\n|\n|\n|")
    elif num == 3:
        print("\n    x-------x\n    |       |\n    |       0\n    |\n    |\n    |")
    elif num == 4:
        print("\n    x-------x\n    |       |\n    |       0\n    |       |\n    |\n    |")
    elif num == 5:
        print("\n    x-------x\n    |       |\n    |       0\n    |      /|\ \n    |      /\n    |")
    elif num == 6:
        print("\n    x-------x\n    |       |\n    |       0\n    |      /|\ \n    |      / \ \n    |")
    else:
        print("Invalid input. Please enter a number between 1-6.")


def main():
    draw_hangman(4)


if __name__ == '__main__':
    main()
