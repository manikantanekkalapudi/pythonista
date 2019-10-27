# Source: https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-Imports/my_module.py
print('Imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
