import sys
from stats import get_word_count, get_word_reps, sorted_dictionary

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book_file = sys.argv[1]
    book = get_book_text(path_to_book_file)
    word_count = get_word_count(book)
    word_reps = get_word_reps(book)
    sorted_word_list = sorted_dictionary(word_reps)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for word_dict in sorted_word_list:
        if word_dict['char'].isalpha():
            print(f"{word_dict['char']}: {word_dict['count']}")
    print("============= END ===============")
            

main()