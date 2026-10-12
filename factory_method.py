
from abc import ABC, abstractmethod


# Загальний клас транспорту
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


# Конкретні види транспорту
class Truck(Transport):
    def deliver(self):
        return "Доставка вантажівкою"


class Ship(Transport):
    def deliver(self):
        return "Доставка кораблем"


# Базовий клас логістики
class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        return transport.deliver()


# Фабрики для різних видів доставки
class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()


# Запуск програми
if __name__ == "__main__":
    road = RoadLogistics()
    sea = SeaLogistics()

    print(road.plan_delivery())
    print(sea.plan_delivery())
