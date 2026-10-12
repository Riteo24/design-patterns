"""Стратегія: спосіб розрахунку доставки можна замінити під час роботи."""
from abc import ABC, abstractmethod


class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate(self, weight_kg):
        pass


class StandardDelivery(DeliveryStrategy):
    def calculate(self, weight_kg):
        return 30 + weight_kg * 5


class ExpressDelivery(DeliveryStrategy):
    def calculate(self, weight_kg):
        return 60 + weight_kg * 10


class DeliveryCalculator:
    def __init__(self, strategy: DeliveryStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: DeliveryStrategy):
        self._strategy = strategy

    def calculate(self, weight_kg):
        if weight_kg < 0:
            raise ValueError("Вага не може бути від'ємною")
        return self._strategy.calculate(weight_kg)


def main():
    calculator = DeliveryCalculator(StandardDelivery())
    print(f"Звичайна доставка 2 кг: {calculator.calculate(2)} грн")
    calculator.set_strategy(ExpressDelivery())
    print(f"Експрес-доставка 2 кг: {calculator.calculate(2)} грн")


if __name__ == "__main__":
    main()
