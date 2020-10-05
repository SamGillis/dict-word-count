# put your code here.

def word_count(text):
    the_file = open(text)
    words_dict = {}
    for line in the_file:
        line = line.rstrip()
        list_words = line.split(' ')

        ##for each words 
        for word in list_words:
            words_dict[word] = words_dict.get(word, 0) + 1
        ##take off any punct

        ##add word to dictionary or update value
    for each in words_dict:
        print(f"{each} {words_dict[each]}")

        ##testing configuration


word_count('twain.txt')