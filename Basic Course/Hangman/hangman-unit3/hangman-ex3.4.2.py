def main():
    # Accept input string from user
    input_str = input("Please enter a string: ")

    # Get the first character of the string
    first_char = input_str[0]

    # Replace all occurrences of the first character with 'e', except for the first character itself
    output_str = first_char + input_str[1:].replace(first_char, 'e')

    # Print the modified string
    print(output_str)


if __name__ == '__main__':
    main()
