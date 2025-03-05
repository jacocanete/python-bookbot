from stats import get_num_char


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    letter_count = get_num_char(file_contents)
    print(f"{letter_count} words found in the document")


main()
