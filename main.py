def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_word_count(book_path)
    print(text)
    print(count)

    
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
    


    
main ()

