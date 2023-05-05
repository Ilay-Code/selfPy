def main():
    temp = input("Insert the temperature you would like to convert: ")

    # check if temperature is in C or F
    if temp[-1] == "C" or temp[-1] == "c":
        c = float(temp[:-1])
        f = (c * 1.8) + 32
        print(f"{f}F")
    elif temp[-1] == "F" or temp[-1] == "f":
        f = float(temp[:-1])
        c = (f - 32) / 1.8
        print(f"{c}C")
    else:
        print("Invalid input. Please use the suffix C or F.")


if __name__ == '__main__':
    main()