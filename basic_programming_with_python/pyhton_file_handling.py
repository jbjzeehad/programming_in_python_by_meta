# file = open(
#     'F:\programming_in_python_by_meta\\basic_programming_with_python\\test.txt', mode='r')
# data = file.readline()
# print(data)
# file.close()

with open('F:\programming_in_python_by_meta\\basic_programming_with_python\\test.txt', mode='r') as file:
    data = file.readline()
    print(data)
