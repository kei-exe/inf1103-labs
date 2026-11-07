from digital_product import DigitalProduct
from physical_product import PhysicalProduct
from supplier import Supplier

supplier = Supplier("S001", "Tech Supplies", "tech@example.com")

physical = PhysicalProduct(
    "P001", "Laptop", 1200.0, 5, 2.5, supplier
)

digital = DigitalProduct(
    "P002", "Game", 30.0, 10, 500.0, supplier
)

del supplier

print(physical.to_dict()["supplier"])
print(digital.to_dict()["supplier"])