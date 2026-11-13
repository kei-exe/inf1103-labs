from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order

supplier = Supplier("S001", "Tech Supplies", "tech@example.com")
physical = PhysicalProduct("P001", "Laptop", 1200.0, 5, 2.5, supplier)
digital = DigitalProduct("P002", "Game", 30.0, 10, 500.0, supplier)

# Section 4: Composition
print("=== COMPOSITION ===")

order1 = Order("ORD001")
order1.add_order_line(physical, 2)
order1.add_order_line(digital, 3)

order2 = Order("ORD002")
order2.add_order_line(physical, 1)

print("Order 1 total:", order1.calculate_total())
print("Order 2 total:", order2.calculate_total())

line1 = order1.get_order_lines()[0]
line2 = order2.get_order_lines()[0]

print("Same OrderLine object:", line1 is line2)
print("Same Product object:", line1.get_product() is line2.get_product())

assert order1.calculate_total() == 2490.0
assert order2.calculate_total() == 1200.0
assert line1 is not line2
assert line1.get_product() is line2.get_product()

order2.remove_order_line(0)
print("Order 2 after removal:", order2.calculate_total())

# Section 6: LSP
print("\n=== LSP ===")

def show_product_details(product: Product) -> None:
    product.display_information()
    print(" |", product.get_fulfilment_info())

show_product_details(physical)
show_product_details(digital)

physical.update_stock(4)
digital.update_stock(9)

assert physical.to_dict()["stock"] == 4
assert digital.to_dict()["stock"] == 9

# Section 7: Polymorphism
print("\n=== POLYMORPHISM ===")

inventory = Inventory()
inventory.add_product(physical)
inventory.add_product(digital)

for product in inventory.get_all_products():
    show_product_details(product)

print("\nAll tests passed!")