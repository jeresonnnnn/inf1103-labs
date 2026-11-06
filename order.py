from Product import Product

class OrderLine:

    def __init__(self, product: Product, quantity: int) -> None:
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive whole number.")
        self.__product: Product = product
        self.__quantity: int = quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> Product:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    def display_line(self) -> None:
        print(f"  {self.__product.get_name():<15} x{self.__quantity:<4} "
              f"@ ${self.__product.get_price():>9.2f} = ${self.calculate_subtotal():>10.2f}")


class Order:
    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] =  []

    def get_order_id(self) -> str:
        return self.__order_id

    def get_order_lines(self) -> list[OrderLine]:
        return list(self.__order_lines)

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> bool:
        for line in self.__order_lines:
            if line.get_product().get_product_id().lower() == product_id.strip().lower():
                self.__order_lines.remove(line)
                return True
        return False

    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self.__order_lines)

    def display_order(self) -> None:
        print(f"\Order {self.__order_id}")
        for line in self.__order_lines:
            line.display_line()
        print(f"    {'TOTAL':<15} {'':<30} ${self.calculate_total():>10.2f}") 