# import abstract class
from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__supplier: Supplier = supplier

    @abstractmethod # every subclass must implement this method
    def get_fulfilment_info(self) -> str:
        pass

    # Convert Product object into a dictionary for JSON storage
    def to_dict(self) -> dict:

        product_details = {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier.to_dict()
        }

        return product_details

    def update_stock(self, quantity: int) -> None:
        if quantity < 0:
            print("Stock cannot be negative.")
            return
    
        self.__stock = quantity

    def display_information(self) -> None:
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}",
            end=""
        )