def inverse_dict(my_dict):
    inverted_dict = {}
    for key, value in my_dict.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]

    for key in inverted_dict:
        inverted_dict[key].sort()

    return inverted_dict


def main():
    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    inverted_dict = inverse_dict(course_dict)
    print(inverted_dict)


if __name__ == '__main__':
    main()
