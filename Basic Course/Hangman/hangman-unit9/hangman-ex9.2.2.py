def copy_file_content(source, destination):
    with open(source, 'r') as f1, open(destination, 'w') as f2:
        f2.write(f1.read())

