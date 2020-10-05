import string 
import sys
import collections

# put your code here.
##implemented using dictionaries
def word_count(text):
    the_file = open(text)
    words_dict = {}
    for line in the_file:
        line = line.rstrip()
        line = line.translate(str.maketrans('', '', string.punctuation))
        
        list_words = line.split(' ')

        ##for each words 
        for word in list_words:
            words_dict[word.lower()] = words_dict.get(word.lower(), 0) + 1
        ##take off any punct

        ##add word to dictionary or update value
    ##print(sorted(words_dict.values()))
    sorted_words = sorted(words_dict.items(), key=lambda x: x[1])
    for each in sorted_words:
        each = each[0]
        print(f'{each} {words_dict[each]}')
    # for each in sorted(words_dict.keys()):
    #     print(f'{each} {words_dict[each]}')

        ##testing configuration


word_count(sys.argv[1])

##implemented using counters

# def word_count(text):
#     the_file = open(text)
#     words_counter = collections.Counter()
#     # the_file = the_file.translate(str.maketrans('', '', string.punctuation))
#     the_file = the_file.read()
#     the_file = the_file.translate(str.maketrans('', '', string.punctuation))
#     the_file = the_file.replace('\n', ' ')
#     print(f"{the_file}")
#     list_words = the_file.split(' ')
   
    
#     for word in list_words:
#         word = word.lower()
#         words_counter[word] += 1

#         ##add word to dictionary or update value
#     for each in words_counter:
#         print(f"{each} {words_counter[each]}")

#         ##testing configuration


# word_count(sys.argv[1])
