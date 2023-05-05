def main():
    bricks = int(input("Enter three digits (each digit for one pig):"))
    units = bricks % 10
    tens = (bricks // 10) % 10
    hundreds = bricks // 100
    print("total number of bricks:" + str(units + tens + hundreds))
    print("brick per pig:" + str((units + tens + hundreds) / 3))
    print("division's remainder:" + str((units + tens + hundreds) % 3))
    print(bool(str((units + tens + hundreds) % 3)))


if __name__ == '__main__':
    main()
