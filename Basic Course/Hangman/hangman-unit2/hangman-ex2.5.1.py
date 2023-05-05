# this func prints the opening for the game
def print_opening():
    MAX_TRIES = 6

    HANGMAN_ASCII_ART = """ 
     Welcome to the game Hangman
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/ 
                                                               """

    print(HANGMAN_ASCII_ART + "\n" + str(MAX_TRIES))


def main():
    print_opening()


if __name__ == '__main__':
    main()
