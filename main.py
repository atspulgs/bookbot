import sys
from stats import CharCount
from stats import get_word_count, get_character_counts, sort_chars


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as file:
        return file.read()


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file: str = sys.argv[1]
    book_contents: str = get_book_text(path_to_file)
    word_count: int = get_word_count(book_contents)
    char_counts: dict[str, int] = get_character_counts(book_contents)
    sorted_char_counts: list[CharCount] = sort_chars(char_counts)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for char in sorted_char_counts:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
    print(f"============= END ===============")


main()
