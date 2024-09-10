def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_word_count(book_path)
    characters = get_char_appearances(book_path)
    sorted_characters = sort_on(characters)
    print("--- Begint report of books/freankenstein.txt ---")
    print(f"{text} words found in the document")
    print(count)
    for char, num in sorted_characters:
        print(f"The '{char}' character was found {num} times")
    print("--- End report ---")

    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_word_count(wordcount):
    count = 0 
    with open(wordcount) as f:
        data = f.read()
        lines = data.split()
        count += len(lines)
    return count

def get_char_appearances(chars):
    char_count = dict()
    with open(chars) as f:
        data = f.read()
        for da in data:
            char_count[da] = char_count.setdefault(da, 0)+1
    return char_count

def sort_on(dict):
    return sorted(dict.items(), key=lambda item: item[1], reverse=True)

    
main ()

