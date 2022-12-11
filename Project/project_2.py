from collections import defaultdict
from typing import List, Any

test_words = ["tea", "eat", "bat", "ate", "arc", "car"]


def group_anagrams(words: List[str]) -> [list, Any]:
    dfdict = defaultdict(list)
    for i in words:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()

# 2 method
def anagrams(words: List[str]) -> dict:
    array = {}
    for i in words:
        sorted_i = " ".join(sorted(i))
        array[sorted_i] = array.get(sorted_i, []) + [i]
    return array


def info():
    """
    that's how it works sorted() --> [a a s s]
    """
    a = "sasa"
    print(sorted(a))
    print(" ".join(sorted(a)))


if __name__ == "__main__":
    print(group_anagrams(test_words))
    print(anagrams(test_words))

