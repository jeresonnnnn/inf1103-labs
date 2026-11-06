from abc import ABC, abstractmethod

from supplier import Supplier

class Product(ABC):

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = float(price)
        self.__stock: int = 0
        self.update_stock(stock)
        self.__supplier: Supplier = supplier  

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def get_supplier(self) -> Supplier:
        return self.__supplier

    def update_stock(self, quantity) -> None:
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Stock must be a non-negative whole number.")
        self.__stock = quantity

    def display_information(self) -> None:
        print(f"ID: {self.__product_id:<6} | Name: {self.__name:<15} | "
              f"Price: ${self.__price:>9.2f} | Stock: {self.__stock}")
        print(f"     Supplier: {self.__supplier.get_name()} "
              f"({self.__supplier.get_contact_email()})")
    
    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    def to_dict(self) -> dict:
            return {
                "product_id": self.__product_id,
                "name": self.__name,
                "price": self.__price,
                "stock": self.__stock,
                "supplier": self.__supplier.to_dict(),
            }