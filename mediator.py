"""Посередник: користувачі спілкуються через чат, не знаючи один одного."""
from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def send(self, sender, message):
        pass


class ChatRoom(Mediator):
    def __init__(self):
        self._users = []

    def register(self, user):
        if user in self._users:
            return
        if user.mediator is not None and user.mediator is not self:
            raise ValueError("Користувач уже зареєстрований в іншому чаті")
        self._users.append(user)
        user.mediator = self

    def send(self, sender, message):
        if sender not in self._users:
            raise ValueError("Відправник не зареєстрований у чаті")
        for user in self._users:
            if user is not sender:
                user.receive(sender.name, message)


class User:
    def __init__(self, name):
        self.name = name
        self.mediator = None
        self.inbox = []

    def send(self, message):
        if self.mediator is None:
            raise ValueError("Спочатку зареєструйтеся в чаті")
        self.mediator.send(self, message)

    def receive(self, sender_name, message):
        self.inbox.append(f"{sender_name}: {message}")


def main():
    chat = ChatRoom()
    vlad, anna, oleg = User("Влад"), User("Анна"), User("Олег")
    for user in (vlad, anna, oleg):
        chat.register(user)
    vlad.send("Привіт усім!")
    for user in (anna, oleg):
        print(f"{user.name} отримує: {user.inbox[-1]}")


if __name__ == "__main__":
    main()
