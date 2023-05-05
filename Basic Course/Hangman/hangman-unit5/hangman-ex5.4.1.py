def func(num1, num2):
    """
    This function receives two numbers, num1 and num2, and returns their sum.
    :param num1: An integer.
    :param num2: An integer.
    :return: The sum of num1 and num2.
    """
    return num1 + num2


def main():
    # Call the function func
    result = func(5, 7)
    print(result)


if __name__ == '__main__':
    help(func)
    main()
