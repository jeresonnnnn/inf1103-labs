class inventory:

    def __init__(self):
        self.__products = []

    def add_products(self, product):
        if self.search_product(product.get_product_id()) is not None:
            raise ValueError(f"Product ID {product.get_product_id()} already exists.")
        self.__products.append(product)

    def search_product(self, keyword):
        keyword = keyword.strip().lower()
        for product in self.__products:
            if product.get_product_id().lower() == keyword:
                return product
        return None

    def search_by_name(self, keyword):
        keyword = keyword.strip().lower()
        return [p for p in self.__products if keyword in p.get_name().lower()]

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return
        for product in self.__products:
            product.display_information()

    def get_products(self):
        return list(self.__products)