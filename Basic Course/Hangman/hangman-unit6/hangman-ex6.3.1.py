def are_lists_equal(list1, list2):
    list1.sort()
    list2.sort()
    return list1 == list2


def main():
    x = [2, 1, 3]
    y = [1, 2, 3]
    print(are_lists_equal(x, y))


if __name__ == '__main__':
    main()
