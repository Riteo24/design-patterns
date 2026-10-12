"""Замісник: перевірка доступу перед викликом справжнього сховища."""
from abc import ABC, abstractmethod


class DocumentService(ABC):
    @abstractmethod
    def read(self, name):
        pass


class DocumentStorage(DocumentService):
    def __init__(self):
        self._documents = {"report.txt": "Конфіденційний звіт"}
        self.read_count = 0

    def read(self, name):
        self.read_count += 1
        return self._documents[name]


class DocumentProxy(DocumentService):
    def __init__(self, storage, role):
        self._storage = storage
        self._role = role

    def read(self, name):
        if self._role != "admin":
            raise PermissionError("Доступ дозволено лише адміністратору")
        return self._storage.read(name)


def main():
    storage = DocumentStorage()
    guest = DocumentProxy(storage, "guest")
    try:
        print(guest.read("report.txt"))
    except PermissionError as error:
        print(error)
    print(DocumentProxy(storage, "admin").read("report.txt"))
    print(f"Звернень до справжнього сховища: {storage.read_count}")


if __name__ == "__main__":
    main()
