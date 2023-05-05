

def choose_word(file_path, index):
    with open(file_path, 'r') as f:
        words = f.read().split()
    num_words = len(set(words))
    index = (index - 1) % len(words)
    secret_word = words[index]
    return num_words, secret_word


def main():
    print(choose_word("files/word_list", 3))


if __name__ == '__main__':
    main()
