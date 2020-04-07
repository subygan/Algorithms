_end = '_end_'

def make_trie(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            print(letter)
            current_dict = current_dict.setdefault(letter, {})
            print(current_dict)
        print()
        current_dict[_end] = _end
    return root

print(make_trie("hello"))

dictionary = dict()
print(dictionary.setdefault("emine","adjfnakjdnf"))
# print(dictionary)