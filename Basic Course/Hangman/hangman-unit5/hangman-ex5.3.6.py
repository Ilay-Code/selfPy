def fix_age(age):
    if age != 15 and age != 16:
        return 0
    return age


def filter_teens(a=13, b=13, c=13):
    if 13 <= a <= 19:
        a = fix_age(a)
    elif 13 <= b <= 19:
        b = fix_age(b)
    elif 13 <= c <= 19:
        c = fix_age(c)
    return a + b + c


def main():
    print(filter_teens(2, 1, 15))


if __name__ == '__main__':
    main()
