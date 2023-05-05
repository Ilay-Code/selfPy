def main():
    s = input("Please enter a string: ")
    half = len(s) // 2
    result = s[:half].lower() + s[half:].upper()
    print(result)


if __name__ == '__main__':
    main()
