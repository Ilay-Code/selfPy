def seven_boom(end_number):
    boom_list = []
    for i in range(end_number + 1):
        if i % 7 == 0 or '7' in str(i):
            boom_list.append('BOOM')
        else:
            boom_list.append(i)
    return boom_list


def main():
    print(seven_boom(17))


if __name__ == '__main__':
    main()
