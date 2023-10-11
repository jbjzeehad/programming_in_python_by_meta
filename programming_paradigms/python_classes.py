# To instantiate an instance object, it is necessary to define a class, declare an instance, and initialize that instance.

class Myclass:
    # pass
    # print('Hello Class')
    a = 5

    # def hello():
    #     print("Hello World")
    def hello(self):
        print("Hello World")


# myclass = Myclass()
myc = Myclass()
# print(Myclass.a)
print(myc.a)
# print(myc.hello()) #output error
print(myc.hello())  # output: Hello World
# also output None because of no return value
# print(a)  # output error
