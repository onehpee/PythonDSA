class ShoppingItem:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        

cart = []

cart.append(ShoppingItem("cookies", 9.99))
cart.append(ShoppingItem("Pizza", 5.99))
cart.append(ShoppingItem("Juice", 4.99))
cart.append(ShoppingItem("crackers", 11.99))
cart.append(ShoppingItem("oatmeal", 7.99))

cart.pop(0)
for obj in cart:
    print(obj.item, obj.price)



