from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory

supplier = Supplier("S001", "Tech Supplies", "tech@example.com")
physical = PhysicalProduct("P001", "Laptop", 1200.0, 5, 2.5, supplier)

# Create two inventories
inventory_a = Inventory()
inventory_b = Inventory()

# Add product to Inventory A
inventory_a.add_product(physical)
print("Inventory A before removal:")
inventory_a.display_all()

# Remove product from Inventory A
inventory_a.remove_product("P001")

print("\nInventory A after removal:")
inventory_a.display_all()

# Check if product still exists
print("\nProduct after removal:")
physical.display_information()

# Add the same product to Inventory B
inventory_b.add_product(physical)

print("\nInventory B after transfer:")
inventory_b.display_all()