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


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def get_num(d):
    return d["num"]


def dict_to_sorted_list(char_count):
    sorted_list = []
    for char in char_count:
        sorted_list.append({"char": char, "num": char_count[char]})
    sorted_list.sort(key=get_num, reverse=True)
    return sorted_list


def print_stats(path):
    file_contents = get_book_text(path)
    word_count = get_num_words(file_contents)
    char_count = get_num_char(file_contents)
    sorted_list = dict_to_sorted_list(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
