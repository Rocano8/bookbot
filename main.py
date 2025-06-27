import sys

from stats import get_num_words
from stats import count_characters_loop
from stats import sort_and_filter_char_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_file = sys.argv[1]


def get_book_text(path_to_file):
    with open(path_to_file, 'r') as file:
        return file.read()



def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    book_text = get_book_text(path_to_file)
    num_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    character_counts = count_characters_loop(book_text)
    char_list = [{"char": char, "num": count} for char, count in character_counts.items()]
    sorted_alpha_list = sort_and_filter_char_list(char_list)
    for item in sorted_alpha_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()