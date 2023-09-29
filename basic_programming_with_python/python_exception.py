def divide_by(a, b):
    return a/b


try:
    ans = divide_by(40, 0)
# except Exception as e:
#     print("Something went wrong!", e)
#     print(e.__class__)
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")
except Exception as e:
    print("Something went wrong!", e)
# print(divide_by(40, 4))
# print(divide_by(40, 0))
