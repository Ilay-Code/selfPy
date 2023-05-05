def mult_tuple(tuple1, tuple2):
    result = ()
    for i in tuple1:
        for j in tuple2:
            result += ((i,j),)
            result += ((j,i),)
    return result

def main():
    first_tuple = (1, 2)
    second_tuple = (4, 5)
    print(mult_tuple(first_tuple, second_tuple))


if __name__ == '__main__':
    main()