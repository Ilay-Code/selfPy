def is_greater(my_list, n):
    lst_greaters = []
    for number in my_list:
        if number > n:
            lst_greaters.append(number)
    return lst_greaters


def main():
    print(is_greater([1, 30, 25, 60, 27, 28], 28))


if __name__ == '__main__':
    main()
