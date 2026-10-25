#Name: Christina Allison
#Date: October 19, 2026
#Purpose: Create an online shopping cart program

class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity 
    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${self.item_quantity * self.item_price:.0f}')
class ShoppingCart:
    def __init__(self, customer_name = "none", current_date = "January 1, 2025"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)
   
    def remove_item(self, name):
        for item in self.cart_items:
            if item.item_name == name:
                self.cart_items.remove(item)
                return 
        print('Item not found in cart. Nothing removed.')

    def modify_item(self, new_item):
        for item in self.cart_items:
            if item.item_name == new_item.item_name:
                item.item_quantity = new_item.item_quantity
                return
        print('Item not found in cart. Nothing modified.')

    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.item_price * item.item_quantity
        return total
   
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return      
        for item in self.cart_items:
            item.print_item_cost()
        item_count = 0
        for item in self.cart_items:
            item_count += item.item_quantity
        print(f"Number of Items: {item_count}")
        print()
        total = self.get_cost_of_cart()
        print(f"Total: ${total:.0f}")
      
def print_menu():
        
        print('MENU') 
        print('a - Add item to cart')
        print('r - Remove item from cart') 
        print('c - Change item quantity')
        print('o - Output shopping cart')      
        print('q - Quit')

def execute_menu(menuOp, theCart):
    if menuOp == 'a':
        print('ADD ITEM TO CART')
        name = input('Enter the item name: ')
        price = int(input('Enter the item price: '))
        quantity = int(input('Enter the item quantity: '))
        new_item = ItemToPurchase(name, price, quantity)
        theCart.add_item(new_item)                       

    elif menuOp == 'r':
        print('REMOVE ITEM FROM CART')
        name = input('Enter name of item to remove: ')
        theCart.remove_item(name)

    elif menuOp == 'c':
        print('CHANGE ITEM QUANTITY')
        name = input('Enter the item name: ')
        quantity = int(input('Enter the new quantity: '))
        new_item = ItemToPurchase(name, 0, quantity)
        theCart.modify_item(new_item)

    elif menuOp == 'o':
        print('OUTPUT SHOPPING CART')
        theCart.print_total()
                
if __name__ == "__main__":
    menu_choice = ' '
    cust_name = input("Enter customer's name: ")
    day_date = input("Enter today's date: ")
    print()
    print(f'Customer name: {cust_name}')
    print(f"Today's date: {day_date}")  
    my_cart = ShoppingCart(cust_name, day_date)
    
    print()
    print_menu()
    print()

    while menu_choice != 'q':
        menu_choice = input('Choose an option:\n')
        if menu_choice in ['a', 'r', 'c', 'o']:
            execute_menu(menu_choice, my_cart)
            print()
            print_#Name: Christina Allison
#Date: October 19, 2026
#Purpose: Create an online shopping cart program

class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity 
    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}')
class ShoppingCart:
    def __init__(self, customer_name = "none", current_date = "January 1, 2025"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)
   
    def remove_item(self, name):
        for item in self.cart_items:
            if item.item_name == name:
                self.cart_items.remove(item)
                return 
        print('Item not found in cart. Nothing removed.')

    def modify_item(self, new_item):
        for item in self.cart_items:
            if item.item_name == new_item.item_name:
                item.item_quantity = new_item.item_quantity
                return
        print('Item not found in cart. Nothing modified.')

    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.item_price * item.item_quantity
        return total
   
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return      
        for item in self.cart_items:
            item.print_item_cost()
        item_count = 0
        for item in self.cart_items:
            item_count += item.item_quantity
        print(f"Number of Items: {item_count}")
        print()
        total = self.get_cost_of_cart()
        print(f"Total: ${total}")
      
def print_menu():
        
        print('MENU') 
        print('a - Add item to cart')
        print('r - Remove item from cart') 
        print('c - Change item quantity')
        print('o - Output shopping cart')      
        print('q - Quit')

def execute_menu(menuOp, theCart):
    if menuOp == 'a':
        print('ADD ITEM TO CART')
        name = input('Enter the item name: ')
        price = int(input('Enter the item price: '))
        quantity = int(input('Enter the item quantity: '))
        new_item = ItemToPurchase(name, price, quantity)
        theCart.add_item(new_item)                       

    elif menuOp == 'r':
        print('REMOVE ITEM FROM CART')
        name = input('Enter name of item to remove: ')
        theCart.remove_item(name)

    elif menuOp == 'c':
        print('CHANGE ITEM QUANTITY')
        name = input('Enter the item name: ')
        quantity = int(input('Enter the new quantity: '))
        new_item = ItemToPurchase(name, 0, quantity)
        theCart.modify_item(new_item)

    elif menuOp == 'o':
        print('OUTPUT SHOPPING CART')
        theCart.print_total()
                
if __name__ == "__main__":
    menu_choice = ' '
    cust_name = input("Enter customer's name: ")
    day_date = input("Enter today's date: ")
    print()
    print(f'Customer name: {cust_name}')
    print(f"Today's date: {day_date}")  
    my_cart = ShoppingCart(cust_name, day_date)
    
    print()
    print_menu()
    print()

    while menu_choice != 'q':
        menu_choice = input('Choose an option:\n')
        if menu_choice in ['a', 'r', 'c', 'o']:
            execute_menu(menu_choice, my_cart)
            print()
            print_menu()
            print()