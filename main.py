import sys
from stats import count_words
from stats import count_chars
from stats import sorted_chars

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) == 2:
        text_of_book = get_book_text(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = count_words(text_of_book)
    num_chars = count_chars(text_of_book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_list_of_chars = sorted_chars(num_chars)
    for sorted_list_of_char in sorted_list_of_chars:
        if sorted_list_of_char["char"].isalpha():
            print(f"{sorted_list_of_char['char']}: {sorted_list_of_char['num']}")
    print("============= END ===============")

main()
