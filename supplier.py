class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
        if not supplier_id or not name:
            raise ValueError("Supplier ID and name cannot be empty.")
        if "@" not in contact_email:
            raise ValueError("Supplier contact email must contain '@'.")
        self.__supplier_id: str = supplier_id
        self.__name: str = name 
        self.__contact_email: str = contact_email

    def get_supplier_id(self) -> str:
        return self.__supplier_id

    def get_name(self) -> str:
        return self.__name

    def get_contact_email(self) -> str:
        return self.__contact_email
        