# или через while
#items = list(words.items())
# i = 0
#while i < len(items):
#     key, value = items[i]
#     print(key * value)
#     i += 1
words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for key in words:
    value = words[key]
    print(key * value)
