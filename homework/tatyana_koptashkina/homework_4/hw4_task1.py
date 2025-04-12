my_dict = {
    'tuple': (1, 2, 'pig', True, 2.22),
    'list': [3, 4, 'cat', False, 3.33],
    'dict': {'one': 2, 2: 'two', 'threee': 3, 'four': True, 'five': 4.44},
    'set': {1, 2, 'one', False, 5.55},
}

# Last element of tuple.
print(my_dict['tuple'][-1])

# Add a new element to the end of the list and remove the second element.
my_dict['list'].append('newelement')
my_dict['list'].pop(1)

# Add a new key and delete one in the dictionary.
my_dict['dict'][('i am a tuple',)] = "new value"
my_dict['dict'].pop('threee')

# Add a new element to the set and delete one if it exists.
my_dict['set'].add(333)
my_dict['set'].discard(1)

print(my_dict)
