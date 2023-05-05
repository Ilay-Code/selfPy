def numbers_letters_count(my_str):
    digits_count = 0
    letters_count = 0

    for char in my_str:
        if char.isdigit():
            digits_count += 1
        elif char.isalpha():
            letters_count += 1

    return [digits_count, letters_count]


def main():
    print(numbers_letters_count("000asdasd"))


if __name__ == '__main__':
    main()
