def chocolate_maker(small, big, x):
    return small + big * 5 == x


def main():
    print(chocolate_maker(3, 1, 9))


if __name__ == '__main__':
    main()
