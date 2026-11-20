
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier


class ProductFactory:
    """Creates products based on the given product type."""

    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
        stock_quantity: int, supplier: Supplier, extra_value: float = 0.0) -> Product:
        """Create a physical or digital product."""

        if product_type.lower() == "physical":
            return PhysicalProduct(
                product_id,
                name,
                price,
                stock_quantity,
                extra_value,
                supplier
            )

        elif product_type.lower() == "digital":
            return DigitalProduct(
                product_id,
                name,
                price,
                stock_quantity,
                extra_value,
                supplier
            )

        else:
            raise ValueError(f"Unknown product type: {product_type}")