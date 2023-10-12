# Define a class called MyFirstClass.

class MyFirstClass():

    # Add a print statement inside it such as “Who wrote this?”.

    print("Who wrote this?")

    # Create a string variable named index and initialize it with a string “Author-Book”.

    index = "Author-Book"

    # Define a function called hand_list() with the help of def keyword.
    # Pass the parameter self to it. And then pass two parameters, philosopher and book to it.

    def hand_list(self, philosopher, book):
        self.philosopher = philosopher
        self.book = book

    # write a print statement using the print() function and pass the class variable by accessing it.

        print(MyFirstClass.index)
        print(self.philosopher + " wrote the book: " + self.book)

# Create and instantiate an object of that class, called whodunnit


whodunnit = MyFirstClass()

#  Call method hand_list() over this object “whodunnit” and pass two values to it namely “Sun Tzu” and “The Art of War”.

whodunnit.hand_list("Jbj", "The Life")
