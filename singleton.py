"""Одинак: усі звернення до Logger() повертають один екземпляр у процесі."""
from threading import Lock


class SingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self._messages = []

    def log(self, message):
        self._messages.append(message)

    def get_messages(self):
        return list(self._messages)


def main():
    first = Logger()
    first.log("Програму запущено")
    second = Logger()
    second.log("Виконано операцію")
    print(f"Один екземпляр: {first is second}")
    for message in first.get_messages():
        print(message)


if __name__ == "__main__":
    main()
