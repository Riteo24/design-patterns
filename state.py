"""Стан: поведінка замовлення і переходи визначаються об'єктом стану."""
from abc import ABC, abstractmethod


class OrderState(ABC):
    @abstractmethod
    def pay(self, order):
        pass

    @abstractmethod
    def ship(self, order):
        pass

    @abstractmethod
    def label(self):
        pass


class NewState(OrderState):
    def pay(self, order):
        order.set_state(PaidState())
        return "Замовлення оплачено"

    def ship(self, order):
        return "Спочатку потрібно оплатити замовлення"

    def label(self):
        return "Нове"


class PaidState(OrderState):
    def pay(self, order):
        return "Замовлення вже оплачено"

    def ship(self, order):
        order.set_state(ShippedState())
        return "Замовлення відправлено"

    def label(self):
        return "Оплачене"


class ShippedState(OrderState):
    def pay(self, order):
        return "Відправлене замовлення вже оплачено"

    def ship(self, order):
        return "Замовлення вже відправлено"

    def label(self):
        return "Відправлене"


class Order:
    def __init__(self):
        self._state = NewState()

    def set_state(self, state: OrderState):
        self._state = state

    def status(self):
        return self._state.label()

    def pay(self):
        return self._state.pay(self)

    def ship(self):
        return self._state.ship(self)


def main():
    order = Order()
    print(f"Стан: {order.status()}")
    print(order.ship())
    print(order.pay())
    print(order.ship())
    print(order.ship())
    print(f"Стан: {order.status()}")


if __name__ == "__main__":
    main()
