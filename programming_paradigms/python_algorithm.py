
# Algorithm for a Palindrome

str = 'racecar'

print(str[0])
print(str[6])

# will checking
# [0] == [6]
# [1] == [5]
# [2] == [4]
# [3] == [3]
print('----------------')


def is_palindrome(str):
    #  working with index
    start_index = 0
    end_index = len(str) - 1

    for x in str:
        if str[start_index] != str[end_index]:
            return False

    return True


# print(is_palindrome('racecar'))
print(is_palindrome('racecars'))
