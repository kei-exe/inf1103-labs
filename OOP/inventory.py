from product import Product

class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = [] # typed list

    # Getter for list of Product objects stored in self.__products
    def get_all_products(self) -> list[Product]:
        return self.__products.copy() # read collection without directly modifying the list

     # Add products to inv
    def add_product(self, product : Product) -> None:
        self.__products.append(product)

    # Remove product from inv
    def remove_product(self, product_id: str) -> None:
        for product in self.__products:
            if product.to_dict()["product_id"] == product_id:
                self.__products.remove(product)
                return

    def search_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.to_dict()["product_id"] == product_id: # Check if product_id matches
                return product

        return None

    def find_product(self, product_id: str) -> Product | None:
        return self.search_product(product_id)

    def display_all(self) -> None:
        if not self.__products: # Check if inventory empty
            print("Inventory is empty.")
            return

        for product in self.__products:
            product.display_information()