# Given a book of words. Assume you have enough main memory to accommodate all words. design a data structure to find top K maximum occurring words.
# The data structure should be dynamic so that new words can be added.

from trie import Trie


def find_k_most_frequent(word: str):
    most_frequents = []
    return most_frequents


if __name__ == '__main__':
    teststr = "the a there anaswe any by their"
    # find_k_most_frequent(teststr)
    t = Trie()
    for s in teststr.split(' '):
        print("Adding({})".format(s))
        t.add(s)

    # Search for different keys
    print("{} ---- {}".format("the", t.search("the")))
    print("{} ---- {}".format("these", t.search("these")))
    print("{} ---- {}".format("their", t.search("their")))
    print("{} ---- {}".format("thaw", t.search("thaw")))
