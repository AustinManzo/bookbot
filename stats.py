



def unique_char(book):
    unique = {}

    text = book.lower()

    for c in text:
        
        if c in unique:
            unique[c] += 1
        else:
            unique[c] = 1
    return unique

def word_count(book):
    num = 0
    words = book.split()
    for w in words:
        num += 1

    return num

def sort_dict_helper(items):
    return items["num"]




def dict_to_sorted_list(char_count):
    new_sorted_list = []
    for char in char_count:
        
    
        num = char_count[char]
        new_dict = {"char": char, "num": num}
        new_sorted_list.append(new_dict)

    new_sorted_list.sort(reverse=True, key=sort_dict_helper)

    return new_sorted_list