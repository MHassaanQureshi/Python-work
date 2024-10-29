class Item:

    def __init__(self,name):
        
            print(name + " total price")

    def calculate_total_price(self,price,quantity):
        return price * quantity



item1 = Item("mobile")
item1.name = "mobile"
item1.price = 2000
item1.quantity = 8
print(item1.calculate_total_price(item1.price,item1.quantity))

item2 = Item("laptop")
item2.name = "laptop"
item2.price = 8000
item2.quantity = 4
print(item2.calculate_total_price(item2.price,item2.quantity))

