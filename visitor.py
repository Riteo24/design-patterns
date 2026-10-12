"""Відвідувач: операції над товарами винесені в окремі класи відвідувачів."""
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Product(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


@dataclass
class Book(Product):
    title: str
    price: int

    def accept(self, visitor):
        return visitor.visit_book(self)


@dataclass
class Electronics(Product):
    name: str
    price: int

    def accept(self, visitor):
        return visitor.visit_electronics(self)


class ProductVisitor(ABC):
    @abstractmethod
    def visit_book(self, book):
        pass

    @abstractmethod
    def visit_electronics(self, electronics):
        pass


class DiscountVisitor(ProductVisitor):
    def visit_book(self, book):
        return book.price * 90 // 100

    def visit_electronics(self, electronics):
        return electronics.price * 95 // 100


class DescriptionVisitor(ProductVisitor):
    def visit_book(self, book):
        return f"Книга '{book.title}'"

    def visit_electronics(self, electronics):
        return f"Електроніка '{electronics.name}'"


def main():
    products = [Book("Основи Python", 300), Electronics("Навушники", 1000)]
    discount = DiscountVisitor()
    description = DescriptionVisitor()
    for product in products:
        print(f"{product.accept(description)}: ціна зі знижкою {product.accept(discount)} грн")


if __name__ == "__main__":
    main()
