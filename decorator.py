"""Декоратор: додавання молока та сиропу через вкладені обгортки."""
from abc import ABC, abstractmethod


class Drink(ABC):
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def cost(self):
        pass


class Coffee(Drink):
    def description(self):
        return "Кава"

    def cost(self):
        return 40


class DrinkDecorator(Drink):
    def __init__(self, drink: Drink):
        self._drink = drink

    def description(self):
        return self._drink.description()

    def cost(self):
        return self._drink.cost()


class Milk(DrinkDecorator):
    def description(self):
        return self._drink.description() + ", молоко"

    def cost(self):
        return self._drink.cost() + 10


class Syrup(DrinkDecorator):
    def description(self):
        return self._drink.description() + ", сироп"

    def cost(self):
        return self._drink.cost() + 5


def main():
    coffee = Coffee()
    decorated = Syrup(Milk(coffee))
    print(f"{coffee.description()}: {coffee.cost()} грн")
    print(f"{decorated.description()}: {decorated.cost()} грн")


if __name__ == "__main__":
    main()
