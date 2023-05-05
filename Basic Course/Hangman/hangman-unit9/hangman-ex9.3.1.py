def my_mp3_playlist(file_path):
    with open(file_path, 'r') as file:
        song_list = [line.strip().split(';') for line in file]

    longest_song = max(song_list, key=lambda x: x[2])

    num_songs = len(song_list)

    performers = [song[1] for song in song_list]
    most_common_performer = max(set(performers), key=performers.count)

    return longest_song[0], num_songs, most_common_performer

def main():
    print(my_mp3_playlist("files/file1"))
if __name__ == '__main__':
    main()