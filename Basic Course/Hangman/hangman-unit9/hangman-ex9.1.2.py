def sort_words(file_path):
    with open(file_path) as f:
        words = f.read().split()
    return sorted(set(words))

def reverse_lines(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    return [line.rstrip()[::-1] for line in lines]

def last_lines(file_path, n):
    with open(file_path) as f:
        lines = f.readlines()
    return lines[-n:]

def main():
    file_path = input("Enter a file path: ")
    task = input("Enter a task: ")
    if task == "sort":
        print(sort_words(file_path))
    elif task == "rev":
        print(reverse_lines(file_path))
    elif task == "last":
        n = int(input("Enter a number: "))
        print("".join(last_lines(file_path, n)))
    else:
        print("Unknown task:", task)

if __name__ == '__main__':
    main()