def shift_left(my_list):
    return [my_list[2], my_list[0], my_list[1]]


def main():
    my_list = [0, 1, "s"]
    shifted_list = shift_left(my_list)
    print(shifted_list)


if __name__ == '__main__':
    main()
