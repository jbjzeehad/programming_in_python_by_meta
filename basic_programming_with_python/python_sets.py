set_a = {1, 2, 3, 4, 5}
print(set_a)  # Out : {1,2,3,4,5}

set_b = {1, 2, 3, 4, 5, 5}
print(set_b)  # Out : {1,2,3,4,5}

set_a.add(6)  # value
print(set_a)  # Out : {1,2,3,4,5,6}

set_a.remove(2)  # value
print(set_a)  # Out : {1,3,4,5,6}

set_a.discard(4)  # value
print(set_a)  # Out : {1,3,5,6}

set_c = {1, 2, 3, 4, 5}
set_d = {4, 5, 6, 7, 8}
print(set_c.union(set_d))  # Out : {1,2,3,4,5,6,7,8}
print(set_c | set_d)  # Out : {1,2,3,4,5,6,7,8}
print(set_c.intersection(set_d))  # Out : {4,5}
print(set_c & set_d)  # Out : {4,5}
print(set_c.difference(set_d))  # Out : {1,2,3}
print(set_c - set_d)  # Out : {1,2,3}
print(set_c.symmetric_difference(set_d))  # Out : {1,2,3,6,7,8}
print(set_c ^ set_d)  # Out : {1,2,3,6,7,8}
print(set_a[0])  # Out: TypeError
