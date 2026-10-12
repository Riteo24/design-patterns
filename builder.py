"""Будівельник: покрокове створення комп'ютера за допомогою директора."""
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Computer:
    cpu: str = ""
    ram_gb: int = 0
    storage_gb: int = 0


class ComputerBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_cpu(self):
        pass

    @abstractmethod
    def build_ram(self):
        pass

    @abstractmethod
    def build_storage(self):
        pass


class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._computer = Computer()

    def build_cpu(self):
        self._computer.cpu = "Intel Core i3"

    def build_ram(self):
        self._computer.ram_gb = 8

    def build_storage(self):
        self._computer.storage_gb = 256

    def get_result(self):
        result = self._computer
        self.reset()  # Наступна збірка не змінює вже готовий комп'ютер.
        return result


class GamingComputerBuilder(OfficeComputerBuilder):
    def build_cpu(self):
        self._computer.cpu = "AMD Ryzen 7"

    def build_ram(self):
        self._computer.ram_gb = 32

    def build_storage(self):
        self._computer.storage_gb = 1000


class Director:
    def construct(self, builder: ComputerBuilder):
        builder.reset()
        builder.build_cpu()
        builder.build_ram()
        builder.build_storage()


def main():
    director = Director()
    for builder in (OfficeComputerBuilder(), GamingComputerBuilder()):
        director.construct(builder)
        computer = builder.get_result()
        print(f"{computer.cpu}, RAM: {computer.ram_gb} ГБ, SSD: {computer.storage_gb} ГБ")


if __name__ == "__main__":
    main()
