"""Ланцюжок обов'язків: заявка передається до відповідного спеціаліста."""
from abc import ABC, abstractmethod


class SupportHandler(ABC):
    def __init__(self):
        self._next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    def handle(self, topic):
        if self.can_handle(topic):
            return self.resolve(topic)
        if self._next is not None:
            return self._next.handle(topic)
        return "Для цієї заявки немає обробника"

    @abstractmethod
    def can_handle(self, topic):
        pass

    @abstractmethod
    def resolve(self, topic):
        pass


class PasswordSupport(SupportHandler):
    def can_handle(self, topic):
        return topic == "password"

    def resolve(self, topic):
        return "Перша лінія: пароль відновлено"


class BillingSupport(SupportHandler):
    def can_handle(self, topic):
        return topic == "billing"

    def resolve(self, topic):
        return "Відділ оплати: платіж перевірено"


class TechnicalSupport(SupportHandler):
    def can_handle(self, topic):
        return topic == "technical"

    def resolve(self, topic):
        return "Технічний відділ: помилку перевірено"


def main():
    first = PasswordSupport()
    first.set_next(BillingSupport()).set_next(TechnicalSupport())
    for topic in ("password", "billing", "technical", "other"):
        print(first.handle(topic))


if __name__ == "__main__":
    main()
