def my_mp4_playlist(file_path, new_song):
    with open(file_path, "r") as f:
        lines = f.readlines()

    while len(lines) < 3:
        lines.append("\n")

    lines[2] = new_song + ";Unknown;\n"

    with open(file_path, "w") as f:
        f.writelines(lines)

    with open(file_path, "r") as f:
        print(f.read())
def main():
    print(my_mp4_playlist("files/file1", "Python Love Story"))
if __name__ == '__main__':
    main()