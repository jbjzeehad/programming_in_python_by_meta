# with open('F:\programming_in_python_by_meta\\basic_programming_with_python\\newtest.txt', 'w') as file:
#     file.write("Hi this is a file created by file")

# multiple lines

# with open('F:\programming_in_python_by_meta\\basic_programming_with_python\\newtest.txt', 'w') as file:
#     file.writelines(['Hi this is a file created by file',
#                     '\nThis is a another line to be added'])


# with open('F:\programming_in_python_by_meta\\basic_programming_with_python\\newtest.txt', 'a') as file:
#     file.writelines(['\nThis is the first line of file',
#                     '\nThis is a another line'])
try:
    with open('nuewtest.txt', 'a') as file:
        file.writelines(['\nThis is the first line',
                        '\nThis is a another line'])
except FileNotFoundError as e:
    print('ERROR', e)
