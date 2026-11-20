from order_line import OrderLine
from product import Product
from discount_strategy import DiscountStrategy, NoDiscount


class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        """Initialize an order with an optional discount strategy."""
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

        if discount is None:
            self.__discount: DiscountStrategy = NoDiscount()
        else:
            self.__discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def get_order_lines(self) -> list[OrderLine]:
        return self.__order_lines.copy()

    def remove_order_line(self, index: int) -> None:
        if index < 0 or index >= len(self.__order_lines):
            raise IndexError("Order line index out of range")

        self.__order_lines.pop(index)

    def calculate_total(self) -> float:
        """Calculate the order total after applying the discount."""
        total: float = 0.0

        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()

        return self.__discount.apply(total)

    def set_discount(self, discount: DiscountStrategy) -> None:
        """Update the discount strategy for the order."""
        self.__discount = discount