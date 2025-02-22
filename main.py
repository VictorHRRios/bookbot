def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_words_in_book(book_as_string):
    return len(book_as_string.split())

def main():
    book = get_book_text("./books/frankenstein.txt")
    word_count = get_words_in_book(book)
    print(f"{word_count} words found in the document")

main()