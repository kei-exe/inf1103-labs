from supplier import Supplier
from product import Product

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f" | Download Size: {self.__download_size} MB")

    def get_fulfilment_info(self) -> str:
        return "This product is a digital download and does not require shipping/is digitally delivered."

    def to_dict(self):
        product_details = super().to_dict()
    
        # add to existing dict
        product_details["product_type"] = "digital"
        product_details["download_size"] = self.__download_size
    
        return product_details