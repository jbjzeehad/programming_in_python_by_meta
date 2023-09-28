my_d = {}
print(type(my_d))  # Out: <class 'dict'>

my_d = {1: 'Test', 'Name': 'Jia'}
print(my_d)
print(my_d[1])  # key's name # Out: Test
my_d[2] = 'Test 2'  # key,value
print(my_d)  # Out: {1: 'Test', 'Name': 'Jia', 2: 'Test 2'}

my_c = {1: 'Test', 'Name': 'Jia', 1: 'Test'}  # duplicate
print(my_c)  # Out: {1: 'Test', 'Name': 'Jia'}

del my_c[1]  # key's name
print(my_c)  # Out: {'Name': 'Jia'}

for x in my_d:
    print(x)  # Out : only key's name

for key, value in my_d.items():
    print(str(key) + " : " + value)
