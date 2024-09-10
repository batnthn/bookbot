def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_word_count(book_path)
    characters = get_char_appearances(book_path)
    print(text)
    print(count)
    print(characters)

    
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


    
main ()

