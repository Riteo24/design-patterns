"""Спостерігач: магазин повідомляє всіх підписаних покупців."""
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, product):
        pass


class Customer(Observer):
    def __init__(self, name):
        self.name = name
        self.messages = []

    def update(self, product):
        self.messages.append(f"{self.name}, товар '{product}' з'явився у продажу")


class Store:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def restock(self, product):
        # Копія списку допускає відписку під час повідомлення.
        for observer in list(self._observers):
            observer.update(product)


def main():
    store = Store()
    anna, vlad = Customer("Анна"), Customer("Влад")
    store.subscribe(anna)
    store.subscribe(vlad)
    store.restock("Ноутбук")
    print(anna.messages[-1])
    print(vlad.messages[-1])
    store.unsubscribe(anna)
    store.restock("Телефон")
    print(vlad.messages[-1])
    print(f"Повідомлень Анні: {len(anna.messages)}")


if __name__ == "__main__":
    main()
