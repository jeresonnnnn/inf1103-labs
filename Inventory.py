from Product import Product

class Inventory:

    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        if self.find_product(product.get_product_id()) is not None:
            raise ValueError(f"Product ID {product.get_product_id()} already exists.")
        self.__products.append(product)

    def remove_product(self, product_id: str) -> Product | None:
        product = self.find_product(product_id)
        if product is not None:
                self.__products.remove(product)
        return product

    def find_product(self, product_id: str) -> Product | None:
        product_id = product_id.strip().lower()
        for product in self.__products:
            if product.get_product_id().lower() == product_id:
                return product
        return None

    def search_by_name(self, keyword: str) -> list[Product]:
        keyword = keyword.strip().lower()
        return [p for p in self.__products if keyword in p.get_name().lower()]

    def display_all(self) -> None:
        if not self.__products:
            print("Inventory is empty.")
            return
        for product in self.__products:
            product.display_information()

    def get_products(self) -> list[Product]:
        return list(self.__products)