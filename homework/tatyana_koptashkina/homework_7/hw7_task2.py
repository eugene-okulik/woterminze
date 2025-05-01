words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

# Вариант с while
# items = list(words.items())
# i = 0
# while i < len(items):
#     key, value = items[i]
#     print(key * value)
#     i += 1

for key in words:
    value = words[key]
    print(key * value)
