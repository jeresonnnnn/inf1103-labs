from Product import Product

class PhysicalProduct(Product):
    BASE_SHIPPING = 5.00
    RATE_PER_KG = 2.00

    def __init__(self, product_id, name, price, stock):
        super().__init__(product_id, name, price, stock)
        weight = float(weight)
        if weight <= 0:
            raise ValueError("Weight must be greater then 0 kg.")
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        return super().display_information()
    print(f"    Type: Physical | Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self):
        return "Physical product: requires storage and physical shipping."

    
