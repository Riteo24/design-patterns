"""Команда: пульт викликає операції лампи через об'єкт команди."""
from abc import ABC, abstractmethod


class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class TurnOnCommand(Command):
    def __init__(self, light):
        self._light = light
        self._previous_states = []

    def execute(self):
        self._previous_states.append(self._light.is_on)
        self._light.turn_on()

    def undo(self):
        if self._previous_states:
            previous = self._previous_states.pop()
            if previous:
                self._light.turn_on()
            else:
                self._light.turn_off()


class RemoteControl:
    def __init__(self):
        self._history = []

    def press(self, command: Command):
        command.execute()
        self._history.append(command)

    def undo(self):
        if self._history:
            self._history.pop().undo()


def main():
    light = Light()
    remote = RemoteControl()
    remote.press(TurnOnCommand(light))
    print(f"Після команди світло увімкнене: {light.is_on}")
    remote.undo()
    print(f"Після скасування світло увімкнене: {light.is_on}")


if __name__ == "__main__":
    main()
