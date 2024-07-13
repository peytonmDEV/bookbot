def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    num_words = num_of_words(text)
    print(f"Number of words in the book: {num_words}")
    
    num_chars = num_of_char(text)
    print_report(num_chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def num_of_words(book):
    words = book.split()
    return len(words)

def num_of_char(book):
    lowered_string = book.lower()
    character_count = {}
    for char in lowered_string:
        if char.isalpha():  
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count

def sort_on(char_dict):
    return char_dict["num"]

def print_report(character_count):
    char_list = [{"char": char, "num": count} for char, count in character_count.items()]
    
    char_list.sort(reverse=True, key=sort_on)
    
    for entry in char_list:
        print(f"The '{entry['char']}' character was found {entry['num']} times")

main()