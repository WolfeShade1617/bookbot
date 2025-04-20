# stats.py
def count_words(text):
    """Count the number of words in text"""
    words = text.split()
    return len(words)

def count_characters(text):
    """Count occurrences of each character"""
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_characters(char_counts):
    """Convert character counts to sorted list of dictionaries"""
    sorted_list = []
    for char, count in char_counts.items():
        if char.isalpha():  # Only include alphabetical characters
            sorted_list.append({"char": char, "count": count})
    # Sort by count (descending)
    sorted_list.sort(reverse=True, key=lambda x: x["count"])
    return sorted_list