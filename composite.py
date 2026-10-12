"""Компонувальник: файли та вкладені папки мають спільну операцію size()."""
from abc import ABC, abstractmethod


class FileSystemItem(ABC):
    @abstractmethod
    def size(self):
        pass


class File(FileSystemItem):
    def __init__(self, name, size_kb):
        self.name = name
        self._size_kb = size_kb

    def size(self):
        return self._size_kb


class Folder(FileSystemItem):
    def __init__(self, name):
        self.name = name
        self._children = []

    def add(self, item: FileSystemItem):
        self._children.append(item)

    def remove(self, item: FileSystemItem):
        self._children.remove(item)

    def size(self):
        return sum(item.size() for item in self._children)


def main():
    documents = Folder("Документи")
    documents.add(File("report.txt", 20))
    photos = Folder("Фото")
    photos.add(File("photo.jpg", 300))
    root = Folder("Коренева папка")
    root.add(documents)
    root.add(photos)
    root.add(File("notes.txt", 10))
    print(f"Розмір документів: {documents.size()} КБ")
    print(f"Розмір усієї папки: {root.size()} КБ")


if __name__ == "__main__":
    main()
