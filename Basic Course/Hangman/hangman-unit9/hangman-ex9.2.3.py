def who_is_missing(file_name):
    with open(file_name, 'r') as f:
        nums = sorted(map(int, f.read().strip().split(',')))

    for i in range(1, len(nums) + 2):
        if i not in nums:
            with open('found.txt', 'w') as f:
                f.write(str(i))
            return i