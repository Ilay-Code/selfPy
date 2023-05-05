def main():
    encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
    decoded_message = encrypted_message[:: -1].replace('X', '')
    print(decoded_message)


if __name__ == '__main__':
    main()
