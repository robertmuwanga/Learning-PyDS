class Entry:
    def __init__(self, input_word, input_synonyms):
        self.word = input_word
        self.input_synonyms = input_synonyms

def search(keyword):
    all_words = [keyword]
    word_count = []
    
    for entry in Therasus:
        if keyword == entry.word :
            for word in entry.input_synonyms:
                all_words.append(word)

    for search_word in all_words:
        count = 0
        for document in Corpus:
            for word in document:
                if search_word == word:
                    count += 1
        word_count.append((search_word, count))

    return word_count # modify to return a list of tuples

Therasus = [
    Entry('dog', ['doggie', 'puppy']),
    Entry('cat', ['kitty'])
]

Corpus = [
    ['this', 'is', 'a', 'single', 'document'],
    ['here', 'is', 'another', 'document'],
    ['the', 'dog', 'doggie', 'is', 'a', 'good', 'boy'],
    ['the', 'cat', 'that', 'has', 'a', 'good', 'kitty', 'and', 'bad', 'kitty']
]

input = 'cat'
output = search(input)
print(output)
# do not remove this line!
