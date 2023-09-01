def get_words_list(string):
    word_list = string.split()
    return word_list

def get_counts(word_list):
    word_counts = dict()
    
    for word in word_list:
        if not word in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    
    return word_counts