menu = ['espresso', 'mocha', 'latto', 'cappuccino', 'cortado', 'americano']


def find_coffee(coffe):
    if coffe[0] == 'c':
        return coffe


# map_coffee = map(find_coffee, menu)
# print(map_coffee)
# for x in map_coffee:
#     print(x)

filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)
