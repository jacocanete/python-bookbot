def get_num_words(file_contents):
    split_words = file_contents.split()
    word_count = len(split_words)
    return word_count


def get_num_char(file_contents):
    char_count = {}

    for char in file_contents.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count
