import random


# this func prints the opening for the game
def print_opening():
    random_attempts = random.randint(5, 10)
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
    print(random_attempts)


def main():
    print_opening()


if __name__ == '__main__':
    main()
