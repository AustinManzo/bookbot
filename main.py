from stats import word_count, unique_char, dict_to_sorted_list
import sys


#takes a filepath as input and returns the contents of the file as a string
def get_book_text(file_path):

    text = file_path.read()

    return text

def word_count(book):
    num = 0
    words = book.split()
    for w in words:
        num += 1

    return num

def main():
    if len(sys.argv) <=1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as relative_path:
        print("============ BOOKBOT ============")
        print("Analyzing book found at ...")
        print("----------- Word Count ----------")
        book = get_book_text(relative_path)
        number = word_count(book)
        num_char = unique_char(book)
        print(f"Found {number} total words")
        sorted_list = dict_to_sorted_list(num_char)
        print("--------- Character Count -------")
        for item in sorted_list:
            if item["char"].isalpha() == False:
                continue
            print(f'{item["char"]}: {item["num"]}')
        print("============= END ===============")
    





main()

