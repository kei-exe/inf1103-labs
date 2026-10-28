from product import Product

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product : Product):
        self.__products.append(product)

    #def search_product():

    def display_all(self):
        if not self.__products: # Check if inventory empty
            print("Inventory is empty.")
            return

        for product in self.__products: # Loop every product in self.__products
            product.display_information() # Print product information