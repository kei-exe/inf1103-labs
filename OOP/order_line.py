from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        # Initialise the attributes
        self.__product: Product = product
        self.__quantity: int = quantity

    def calculate_subtotal(self) -> float:
        # Return the product's price multiplied by the quantity
        return self.__product.get_price * self.__quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> int:
        return self.__quantity