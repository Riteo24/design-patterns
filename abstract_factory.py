from abc import ABC, abstractmethod


# Абстрактні типи елементів інтерфейсу
class Button(ABC):
    @abstractmethod
    def draw(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def draw(self):
        pass


# Елементи для Windows
class WindowsButton(Button):
    def draw(self):
        return "Кнопка Windows"


class WindowsCheckbox(Checkbox):
    def draw(self):
        return "Прапорець Windows"


# Елементи для macOS
class MacButton(Button):
    def draw(self):
        return "Кнопка macOS"


class MacCheckbox(Checkbox):
    def draw(self):
        return "Прапорець macOS"


# Абстрактна фабрика
class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


# Конкретні фабрики
class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacFactory(UIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


def show_interface(factory):
    print(factory.create_button().draw())
    print(factory.create_checkbox().draw())


if __name__ == "__main__":
    print("Інтерфейс Windows:")
    show_interface(WindowsFactory())

    print("\nІнтерфейс macOS:")
    show_interface(MacFactory())
