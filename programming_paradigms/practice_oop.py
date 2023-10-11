class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self, rate):
        print(self.num_rooms)
        cost = rate * self.num_rooms
        return cost
        # pass
        # Functionality to calculate the costs from the area of the house


house = House()
print(house.num_rooms)  # Ou: 5
print(House.num_rooms)  # Ou: 5
house.num_rooms = 7
print(house.num_rooms)  # Ou: 7
print(House.num_rooms)  # Ou: 5
House.num_rooms = 8
print(house.num_rooms)  # Ou: 7
print(House.num_rooms)  # Ou: 8

# pass keyword allows the program to continue execution without impacting any functionality or flow. It can be used in class ,function declarations as well as conditional statements.
