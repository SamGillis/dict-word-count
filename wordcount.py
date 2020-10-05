# put your code here.

def word_count(text):
    the_file = open(text)
    words_dict = {}
    for line in the_file:
        line = line.rstrip()
        list_words = line.split(' ')

        ##for each words 

        ##take off any punct

        ##add word to dictionary or update value
