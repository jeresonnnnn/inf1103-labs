from Product import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        download_size = float(download_size)
        if download_size <= 0:
            raise ValueError("Download size must be greater then 0 MB.")
        self.__download_size: float = download_size

    def get_download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"     Type: Digital | Download size: {self.__download_size:.2f} MB")

    def get_fulfilment_info(self) -> str:
        return "Digital product: delivered through a download link, no shipping."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data

    @classmethod
    def from_dict(cls, data: dict, supplier: Supplier) -> "DigitalProduct":
        return cls(data["product_id"], data["name"], data["price"], data["stock"], data["download_size"], supplier)