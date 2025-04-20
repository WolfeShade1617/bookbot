# main.py
import sys
from pathlib import Path
from stats import count_words, count_characters, sort_characters

def print_report(book_path, word_count, char_counts):
    """Print formatted analysis report"""
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    sorted_chars = sort_characters(char_counts)
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['count']}")
    
    print("============= END ===============")

def main():
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = Path(sys.argv[1])
    try:
        text = book_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: File {book_path} not found")
        sys.exit(1)
    
    word_count = count_words(text)
    char_counts = count_characters(text)
    
    print_report(book_path, word_count, char_counts)

if __name__ == "__main__":
    main()