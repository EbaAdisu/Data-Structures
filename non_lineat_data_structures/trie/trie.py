# still working in it

from collections import Counter, defaultdict, deque
trie = defaultdict(int)


def insert(trie, word):
    cur = trie
    for char in word:
        if char not in cur:
            cur[char] = defaultdict(int)
        cur = cur[char]
    cur['is_end'] = True
    cur['word_end'] += 1


def search(trie, word):
    cur = trie
    for char in word:
        if char not in cur:
            return False
        cur = cur[char]
    return cur['is_end'] == True


def startsWith(trie, prefix):
    cur = trie
    for char in prefix:
        if char not in cur:
            return False
        cur = cur[char]
    return True

# a lots of things to add in delete like remove the is_end bool


def deleteWord(trie, word):
    cur = trie
    pre = trie
    for char in word:
        pre = cur
        if char not in cur:
            break
        cur = cur[char]
        cur['prefix'] -= 1
        if cur['prefix'] <= 0:
            del pre[char]
    cur['is_end'] = False
