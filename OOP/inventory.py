from product import Product

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product : Product): # Add products to inv
        self.__products.append(product)

    def search_product(self, product_id: str):
        for product in self.__products: # Loop through all products in self.__products
            if product.get_product_id() == product_id: # Check if product_id matches
                return product # return if match

        return None # return nothing if don't match

    def display_all(self):
        if not self.__products: # Check if inventory empty
            print("Inventory is empty.")
            return

        for product in self.__products: # Loop every product in self.__products
            product.display_information() # Print product information