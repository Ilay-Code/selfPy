def are_files_equal(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        return f1.read() == f2.read()

def main():
    print(are_files_equal("file1","file2"))
if __name__ == '__main__':
    main()