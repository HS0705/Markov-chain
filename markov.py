"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    opened_file = open(file_path)
    text_string = opened_file.read()

    return(text_string)



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    
    chains = {}


    # your code goes here
    words_list = text_string.split()
    words_list.append(None)
    #print(words_list)


    for word in range(0,len(words_list)-2):
        bi_word = (words_list[word], words_list[word+1])

        chains[bi_word] = chains.get(bi_word,[])+ [words_list[word+2]]
    return chains



        

def make_text(chains):
    """Return text from chains."""

    # randomly pick a bi_word
    # randomly pick a value that applies to the chosen bi_word
    # search for the bi_word that had the second value of the first chosen bi_and the value
    # keep repeating lines 1 and 2 until we hit None

    words = []


    # your code goes here



    base_bi_word = choice(list(chains.keys()))
    words.append(base_bi_word[0]) #unpack the tuple
    words.append(base_bi_word[1])
    next_word = choice(chains[base_bi_word])
    
    while next_word != None:
        words.append(next_word)
        base_bi_word = (words[-2],words[-1])
        next_word = choice(chains[base_bi_word])
        





    return(" ".join(words))
    
    
    # print(" ".join(words))


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
