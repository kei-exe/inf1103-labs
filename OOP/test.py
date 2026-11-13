from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order


supplier = Supplier("S001", "Tech Supplies", "tech@example.com")

physical = PhysicalProduct(
    "P001", "Laptop", 1200.0, 5, 2.5, supplier
)

digital = DigitalProduct(
    "P002", "Game", 30.0, 10, 500.0, supplier
)


# SECTION 4: COMPOSITION

print("\n=== COMPOSITION TEST ===")

order1 = Order("ORD001")
order1.add_order_line(physical, 2)
order1.add_order_line(digital, 3)

print("Order 1 total:", order1.calculate_total())

order2 = Order("ORD002")
order2.add_order_line(physical, 1)

print("Order 2 total:", order2.calculate_total())

assert order1.calculate_total() == 2490.0
assert order2.calculate_total() == 1200.0

print("Composition tests passed!")


# SECTION 6: LISKOV SUBSTITUTION PRINCIPLE

print("\n=== LSP TEST ===")

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


show_product_details(physical)
show_product_details(digital)

print("LSP tests passed!")


# SECTION 7: POLYMORPHISM

print("\n=== POLYMORPHISM TEST ===")

products: list[Product] = [physical, digital]

for product in products:
    product.display_information()
    print(product.get_fulfilment_info())

print("Polymorphism tests passed!")