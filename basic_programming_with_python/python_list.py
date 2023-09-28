
list1 = [1, 2, 3, 4, 5]

print(list1[2])  # index

list2 = ['A', 'B', 'C']

list3 = ['Hello', 1, True, 45.20]

list4 = ['Hello', [1, 2, 3], True, 45.20]  # list in list

print(*list1)  # Out: 1 2 3 4 5

print(*list1, sep=",")  # Out: 1,2,3,4,5

print(list1)  # Out: [1,2,3,4,5]

list1.insert(len(list1), 3)  # index, value

print(list1)  # Out: [1,2,3,4,5,3]

list1.insert(1, 3)

print(list1)  # Out : [1,3,2,3,4,5,3]

list1.append(9)  # value

print(list1)  # Out: [1,3,2,3,4,5,3,9]

list1.extend([6, 7, 8, 9])  # value

print(list1)  # Out: [1,3,2,3,4,5,3,9,6,7,8,9]

list1.pop(4)  # index

print(list1)  # Out: [1,3,2,3,5,3,9,6,7,8,9]

del list1[2]  # index

print(list1)  # Out: [1,3,3,5,3,9,6,7,8,9]

for x in list1:
    print('Value:', x)  # index by from 0 to end of the list
