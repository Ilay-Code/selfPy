def last_early(my_str):
    last_char = my_str[-1]
    count = my_str.count(last_char)
    if count > 1:
        return True
    return False


def main():
    print(last_early("ilayf"))


if __name__ == '__main__':
    main()
