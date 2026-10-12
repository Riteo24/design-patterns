"""Міст: тип повідомлення та спосіб його надсилання розвиваються окремо."""
from abc import ABC, abstractmethod


class MessageSender(ABC):
    @abstractmethod
    def send(self, text):
        pass


class EmailSender(MessageSender):
    def send(self, text):
        return f"Email: {text}"


class SmsSender(MessageSender):
    def send(self, text):
        return f"SMS: {text}"


class Notification:
    def __init__(self, sender: MessageSender):
        self._sender = sender  # Міст до незалежної ієрархії реалізацій.

    def notify(self, text):
        return self._sender.send(text)


class UrgentNotification(Notification):
    def notify(self, text):
        return self._sender.send(f"ТЕРМІНОВО! {text}")


def main():
    for sender in (EmailSender(), SmsSender()):
        print(Notification(sender).notify("Замовлення готове"))
        print(UrgentNotification(sender).notify("Збій системи"))


if __name__ == "__main__":
    main()
