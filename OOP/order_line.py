from product import Product


class OrderLine:
    """Stores a product and its ordered quantity."""

    def __init__(self, product: Product, quantity: int) -> None:
        """Create an order line for a product."""
        self.__product: Product = product

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        self.__quantity: int = quantity

    def calculate_subtotal(self) -> float:
        """Calculate the subtotal for this product."""
        return self.__product.get_price * self.__quantity

    def get_product(self) -> Product:
        """Return the product in this order line."""
        return self.__product

    def get_quantity(self) -> int:
        """Return the ordered quantity."""
        return self.__quantity