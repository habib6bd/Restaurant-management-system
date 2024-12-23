from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded !!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item Added")
        else:
            print("Item not Found")

    def view_cart(self):
        print("**View Cart")
        print("Name\tprice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price: {self.cart.total_price}")

class Order:
    def __init__(self) -> None:
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity #If item already added to cart
        else:
            self.items[item] = item.quantity #If item not added to cart

    def remove(self, item):
        if item in self.items:
            del self.items[item]
    
    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def clear(self):
        self.items = {}


class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)
    
    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self, restaurant, item):
        restaurant.menu.remove_item(item)
        

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = [] #database
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} is added !!") #employee.name or only name ek e kotha

    def view_employee(self):
        print("Employee List!!")
        for emp in self.employees:
            print(emp.name, emp.phone, emp.email, emp.address)

class Menu:
    def __init__(self):
        self.items = [] #items er database

    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items: 
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item deleted")
        else:
            print("Item not found")

    def show_menu(self):
        print("******Menu******")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# ad = Admin("Habib", 23456, "habib@gmail.com", "Dhaka")
# ad.add_employee("Nahid", 23456, "nahid@gmail.com", "Gazipur", 23, "Volunteer", 12000)
# ad.view_employee()

mamar_res = Restaurant("Mamar Resturant")
mn = Menu()
item = FoodItem("Pizza", 12.10, 10)
item2 = FoodItem("Burger", 10, 30)

admin = Admin("Rahim", 134535, "rahim@gmail.com", "cha")
admin.add_new_item(mamar_res, item)
admin.add_new_item(mamar_res, item2)

customer1 = Customer("Nahid", 134535, "nahid@gmail.com", "Dhaka")
customer1.view_menu(mamar_res)

item_name = input("Enter Item Name: ")
item_quantity = int(input("Enter Item Quantity: "))

customer1.add_to_cart(mamar_res,item_name, item_quantity)
customer1.view_cart()



