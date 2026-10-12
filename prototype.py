"""Прототип: новий документ створюється клонуванням готового об'єкта."""
from abc import ABC, abstractmethod
from copy import deepcopy
from dataclasses import dataclass, field


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


@dataclass
class Document(Prototype):
    title: str
    sections: list = field(default_factory=list)

    def clone(self):
        # Глибока копія робить вкладений список незалежним від оригіналу.
        return deepcopy(self)


def main():
    original = Document("Шаблон звіту", ["Вступ", "Висновки"])
    copied = original.clone()
    copied.title = "Звіт студента"
    copied.sections.insert(1, "Практична частина")
    print(f"Оригінал: {original.title}: {', '.join(original.sections)}")
    print(f"Копія: {copied.title}: {', '.join(copied.sections)}")
    print(f"Різні об'єкти: {original is not copied}")


if __name__ == "__main__":
    main()
