from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        # Initialise the attributes
        self.__product = product
        self.__quantity = quantity