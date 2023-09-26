
# for i in range(10):
#     print('Looping..', i)

fav = ['creme', 'jonh', 'appple', 'churros', 'tirmun', 'cake']

# for item in fav:
#     print("I like this desert ", item)

# counter = 0
# while counter < len(fav):
#     print('I like this', fav[counter])
#     counter += 1

for id_value, item in enumerate(fav):
    print("I like this desert  ", id_value, item)
