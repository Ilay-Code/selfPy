def main():
    data = ("self.py", 1.543)
    format_string = "Hello %s learner, you have only %.1f units left before you master the course!"
    print(format_string % (data[0], data[1]))


if __name__ == '__main__':
    main()
