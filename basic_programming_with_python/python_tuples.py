
my_tuple = (1, 'strings', 4.5, True)

print(my_tuple[1])  # index

print(type(my_tuple))  # Out: <class 'tuple>

print(my_tuple.count(4.5))  # Out: 1 search value

print(my_tuple.index(4.5))  # Out: 2 search value's index

for x in my_tuple:
    print(x)  # Out: print all value in new line

my_tuple[0] = 5  # type error
