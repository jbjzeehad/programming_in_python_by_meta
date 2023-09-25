# camel naming: myName

# snake naming: my_name

a = b = c = d = 10
print(a)
print(b)
print(c)
print(d)

del d

a, b, c = 91, 82, 73
print(a)
print(b)
print(c)
print(d)
# output: d is not defined. >> because we delete it
