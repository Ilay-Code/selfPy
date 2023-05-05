def main():
    word = input("Please enter a string: ")
    if word.lower() == word[::-1].lower():
        print("OK")
    else:
        print("NOT")
if __name__ == '__main__':
    main()