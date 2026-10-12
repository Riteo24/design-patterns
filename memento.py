"""Знімок: редактор зберігає та відновлює текст, історія зберігає лише знімки."""
from dataclasses import dataclass


class Editor:
    @dataclass(frozen=True)
    class _Snapshot:
        __owner: object
        __text: str

        def _restore(self, editor):
            if editor is not self.__owner:
                raise ValueError("Знімок належить іншому редактору")
            editor._Editor__text = self.__text

    def __init__(self):
        self.__text = ""

    def write(self, text):
        self.__text = text

    def read(self):
        return self.__text

    def save(self):
        return self._Snapshot(self, self.__text)

    def restore(self, snapshot):
        if not isinstance(snapshot, self._Snapshot):
            raise TypeError("Очікується знімок редактора")
        snapshot._restore(self)


class History:
    def __init__(self, editor):
        self._editor = editor
        self._snapshots = []

    def backup(self):
        # Історія не читає і не змінює внутрішній текст знімка.
        self._snapshots.append(self._editor.save())

    def undo(self):
        if not self._snapshots:
            return False
        self._editor.restore(self._snapshots.pop())
        return True


def main():
    editor = Editor()
    history = History(editor)
    editor.write("Перший варіант")
    history.backup()
    editor.write("Другий варіант")
    print(f"До відновлення: {editor.read()}")
    history.undo()
    print(f"Після відновлення: {editor.read()}")


if __name__ == "__main__":
    main()
