"""Адаптер: перетворення інтерфейсу старого сервісу оплати."""
from abc import ABC, abstractmethod
from decimal import Decimal


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class LegacyPaymentService:
    # Старий сервіс приймає ціле число копійок, а не гривні.
    def make_payment(self, amount_in_kopecks):
        return f"Старий сервіс отримав {amount_in_kopecks} копійок"


class PaymentAdapter(PaymentProcessor):
    def __init__(self, legacy_service):
        self._legacy_service = legacy_service

    def pay(self, amount):
        value = Decimal(str(amount))
        if not value.is_finite() or value < 0:
            raise ValueError("Сума має бути скінченною і невід'ємною")
        kopecks = value * 100
        if kopecks != kopecks.to_integral_value():
            raise ValueError("Сума може мати не більше двох десяткових знаків")
        return self._legacy_service.make_payment(int(kopecks))


def checkout(processor: PaymentProcessor, amount):
    return processor.pay(amount)


def main():
    processor = PaymentAdapter(LegacyPaymentService())
    print(checkout(processor, "125.50"))


if __name__ == "__main__":
    main()
