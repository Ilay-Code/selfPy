def squared_numbers(start, stop):
    lst = []
    while start <= stop:
        lst.append(start ** 2)
        start += 1
    return lst


def main():
    print(squared_numbers(4, 8))


if __name__ == '__main__':
    main()
