from order_line import OrderLine
from product import Product


class Order:
    def __init__(self, order_id: str) -> None:
        self.__order_id = order_id
        self.__order_lines: list[OrderLine] = []

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
        total = 0.0

        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()

        return total