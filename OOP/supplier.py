class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
        self.__supplier_id = supplier_id
        self.__name = name
        self.__contact_email = contact_email

    def display_information(self) -> None:
        print(f"Supplier ID: {self.__supplier_id} | ",
              f"Name: {self.__name} | ",
              f"Contact Email: {self.__contact_email}"
        )

    def to_dict(self) -> dict:
        supplier_details = {
            "supplier_id": self.__supplier_id,
            "name": self.__name,
            "contact_email": self.__contact_email
        }
        return supplier_details