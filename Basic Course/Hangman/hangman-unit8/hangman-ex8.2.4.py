def sort_anagrams(list_of_strings):
    lists = []
    for i, word1 in enumerate(list_of_strings):
        if word1 is None:
            continue
        anagram_list = [word1]
        for j, word2 in enumerate(list_of_strings[i+1:]):
            if word2 is None:
                continue
            if sorted(word1) == sorted(word2):
                anagram_list.append(word2)
                list_of_strings[i+j+1] = None
        lists.append(anagram_list)
    return lists
def main():
    list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters',
                     'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    print(sort_anagrams(list_of_words))


if __name__ == '__main__':
    main()