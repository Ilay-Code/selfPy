def main():
    word = input("Please enter a word: ")
    result = " ".join(["_" for letter in word])
    print(result)
if __name__ == '__main__':
    main()