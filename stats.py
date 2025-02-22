def sort_on(dict):
    return dict["count"]

def get_word_count(book_as_string):
    return len(book_as_string.split())

def get_word_reps(book_as_string):
    book_as_array = book_as_string.split()
    word_reps = {}
    for word in book_as_array:
        for char in word.lower():
            word_reps[char] = word_reps.get(char, 0) + 1
    return word_reps

def sorted_dictionary(word_reps):
    word_list = []
    for word in word_reps:
        word_list.append({
            'char' : word,
                'count' : word_reps[word]
                })
    word_list.sort(reverse=True, key=sort_on)
    print(word_list)
    return word_list