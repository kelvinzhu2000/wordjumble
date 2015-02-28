# Read in the word list from the dictionary file
def read_word_list():
    word_list = []
    f = open('word-list', 'r')
    for line in f:
        word_list.append(line.strip())
    f.close()
    return word_list

# Get the list of words from a dictionary in the jumble
def find_words(jumble):
    dictionary = read_word_list()
    found_words = []

    jumble_list = find_jumble_list(jumble)

    # Decided to loop through the words in the dictionary instead of the
    # jumble list because it both avoids getting duplicate words and
    # if the jumble word is long, then the jumble_list can easily become huge
    for word in dictionary:
        if word in jumble_list:
            found_words.append(word)

    return found_words

# Get the whole list of combinations of letters in the jumble
def find_jumble_list(jumble):
    char_list = list(jumble)
    jumble_list = []

    for char in jumble:
        # remove the character from the list of available characters to use
        char_list.remove(char)

        if not char_list:
            jumble_list = jumble_list + [char]
        else:
            combo_list = find_jumble_list("".join(char_list))
            jumble_list = jumble_list + \
                          combo_list + \
                          [append_to_front(char, combo) for combo in combo_list]

        # add the character back to the list of available characters to use
        char_list.append(char)

    return jumble_list

def append_to_front(char, value):
    return char + value
