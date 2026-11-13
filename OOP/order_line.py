from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        # Initialise the attributes
        self.__product = product
        self.__quantity = quantity

    def calculate_subtotal(self) -> float:
    # Return the product's price multiplied by the quantity
        return self.__product.get_price * self.__quantity