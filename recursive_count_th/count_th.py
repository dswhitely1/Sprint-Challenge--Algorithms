'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# Understand

# Plan
# Have 1 pointer starting at 0, look at the word through the index of word[i:i+2].
# Base Case is when the index+2 > len(word)

index = 0
count = 0


def count_th(word):
    global count, index
    if index + 2 > len(word):
        ind_count = count
        count = 0
        index = 0
        return ind_count
    if word[index:index+2] == 'th':
        count += 1
    index += 1
    return count_th(word)


