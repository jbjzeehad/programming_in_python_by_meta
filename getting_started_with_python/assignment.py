# # # Using explicit type conversion, change the following
# # # inputs so the types match with the following below
# # #
# # # name = type string
# # # age = type int
# # # height = type float
# # # loyalty = type boolean

# # # Modify the line below
# # name = input('What is your name? ')

# # print(f"Type of name variable is: {type(name)}. It should be <class 'str'>")

# # # Modify the line below
# # age = int(input('What is your age? '))

# # print(f"Type of age variable is: {type(age)}. It should be <class 'int'>")

# # # Modify the line below
# # height = float(input('What is your height in meters? '))

# # print(
# #     f"Type of height variable is: {type(height)}. It should be <class 'float'>")

# # # Modify the line below
# # loyalty = bool(input('Are you part of our loyalty program? '))

# # print(
# #     f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")
# # #######################################################
# # The below script will ask for 3 inputs. Each input will be based
# # on the price of the items - the price is determined by you. The output
# # should print the total of the 3 inputs rounded to 2 decimal places e.g
# #
# #   1 coffee @ $ 2.00
# #   1 sandwich @ $ 4.99
# #   1 cake @ $ 2.75
# #
# #   Your total bill is $ 9.74

# # Modify the line below
# coffee = float(input('1 coffee @: $ '))

# # Modify the line below
# sandwich = float(input('1 sandwich @: $ '))

# # Modify the line below
# cake = float(input('1 cake @: $ '))

# bill_total = coffee + sandwich + cake

# print('Your total bill is $', float(bill_total))

# a = isinstance(str, "aa")
# print(a)
##############################################

menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee',
        "price": 2.50},
    3: {"name": 'cake',
        "price": 2.79},
    4: {"name": 'soup',
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}


def calculate_subtotal(order):
    """ Calculates the subtotal of an order

    [IMPLEMENT ME] 
        1. Add up the prices of all the items in the order and return the sum

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        float = The sum of the prices of the items in the order
    """
    print('Calculating bill subtotal...')
    # WRITE SOLUTION HERE

    raise NotImplementedError()


def calculate_tax(subtotal):
    """ Calculates the tax of an order

    [IMPLEMENT ME] 
        1. Multiply the subtotal by 15% and return the product rounded to two decimals.

    Args:
        subtotal: the price to get the tax of

    Returns:
        float - The tax required of a given subtotal, which is 15% rounded to two decimals.
    """
    print('Calculating tax from subtotal...')
    # WRITE SOLUTION HERE

    raise NotImplementedError()


def summarize_order(order):
    """ Summarizes the order

    [IMPLEMENT ME]
        1. Calculate the total (subtotal + tax) and store it in a variable named total (rounded to two decimals)
        2. Store only the names of all the items in the order in a list called names
        3. Return names and total.

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        tuple of names and total. The return statement should look like 

        return names, total

    """
    print_order(order)
    # WRITE SOLUTION HERE

    raise NotImplementedError()

# This function is provided for you, and will print out the items in an order


def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

# This function is provided for you, and will display the menu


def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(
            f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you, and will create an order by prompting the user to select menu items


def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' +
                     str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order


'''
Here are some sample function calls to help you test your implementations.
Feel free to change, uncomment, and add these as you wish.
'''


def main():
    order = take_order()
    print_order(order)

    # subtotal = calculate_subtotal(order)
    # print("Subtotal for the order is: " + str(subtotal))

    # tax = calculate_tax(subtotal)
    # print("Tax for the order is: " + str(tax))

    # items, subtotal = summarize_order(order)


if __name__ == "__main__":
    main()
