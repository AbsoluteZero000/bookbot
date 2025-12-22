from stats import count_words, count_chars
import sys

def print_report(path):
    text = get_book_text(path)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    words = count_words(text)
    print(f"Found {words} total words")
    chars = count_chars(text)
    print("--------- Character Count -------")

    [print(f"{key}: {value}") for key, value in chars.items()]


def get_book_text(path):
    with open(path, "r") as file:
        return file.read()




def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print_report(path)


if __name__ == "__main__":
    main()

