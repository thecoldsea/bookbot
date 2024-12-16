def main():
    book1_path = "books/frankenstein.txt"
    #print(contents)

    count_each_character(book1_path)

def open_book(path):
    with open(path) as f:
        return f.read()
    
def count_words(file):
    split_to_list = file.split()
    return len(split_to_list)

def sort_on(dict):
    return dict["num"]

def count_each_character(book_path): # lowercase and iterate single letter in str file > use if to count letters and add to dict
    dict_of_letter_count = {}
    whole_book_1string = open_book(book_path) # fetches the book file
    for letter in whole_book_1string: # takes every letter one by one
        lowered = letter.lower()
        if letter.isalpha(): # check the str if it's alphabetic
            if lowered in dict_of_letter_count:
                dict_of_letter_count[lowered] += 1
            else:
                dict_of_letter_count[lowered] = 1
    list_of_dictionaries = []
    for i in dict_of_letter_count: # iterates through each key in dictionary = i is key
        #print(dict_of_letter_count[i]) # enters key to access value
        list_of_dictionaries.append({"name":i, "num":dict_of_letter_count[i]})
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(whole_book_1string)} words found in the document")
    print("")
    for i in list_of_dictionaries:
        print(f"The '{i['name']}' character was found {i['num']} times")
    print("--- End report ---")
    return list_of_dictionaries
    #return dict_of_letter_count
    
    
    


main()