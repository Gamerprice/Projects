file = open("sample.txt", "r")
words = []
anagram_group = {}

for i in file:
    words.append(i.strip())

for word in words:
    key = ''.join(sorted(word))
    if key in anagram_group:
        anagram_group[key] += word + ' '
    else:
        anagram_group[key] = word + ' '

for group in anagram_group.values():
    print(group.strip())