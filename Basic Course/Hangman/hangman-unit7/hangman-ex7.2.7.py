def arrow(my_char, max_length):
    result = []
    for i in range(1, max_length + 1):
        result.append(my_char * i)
        if i == max_length:
            break
    for i in range(max_length - 1, 0, -1):
        result.append(my_char * i)
    return '\n'.join(result)


def main():
    print(arrow('b', 7))


if __name__ == '__main__':
    main()
