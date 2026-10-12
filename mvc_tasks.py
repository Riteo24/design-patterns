"""MVC: консольний список завдань з окремими Model, View і Controller.

Запуск: python mvc_tasks.py
Демонстрація без ручного введення: python mvc_tasks.py --demo
Дані зберігаються в пам'яті лише під час роботи програми.
"""
import argparse
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Task:
    task_id: int
    title: str
    completed: bool = False


class TaskModel:
    """Model: дані, правила зміни завдань і повідомлення про зміни."""

    def __init__(self):
        self._tasks = {}
        self._next_id = 1
        self._listeners = []

    def get_tasks(self):
        # Незмінні Task і tuple не дають View випадково змінити дані.
        return tuple(self._tasks.values())

    def subscribe(self, listener):
        if listener not in self._listeners:
            self._listeners.append(listener)

    def _notify_changed(self):
        for listener in tuple(self._listeners):
            listener()

    def add_task(self, title):
        clean_title = title.strip()
        if not clean_title:
            raise ValueError("Назва завдання не може бути порожньою.")
        task = Task(self._next_id, clean_title)
        self._tasks[task.task_id] = task
        self._next_id += 1
        self._notify_changed()
        return task

    def _get_task(self, task_id):
        if task_id not in self._tasks:
            raise ValueError(f"Завдання №{task_id} не знайдено.")
        return self._tasks[task_id]

    def toggle_task(self, task_id):
        task = self._get_task(task_id)
        self._tasks[task_id] = replace(task, completed=not task.completed)
        self._notify_changed()

    def delete_task(self, task_id):
        self._get_task(task_id)
        del self._tasks[task_id]
        self._notify_changed()


class TaskView:
    """View: показує дані моделі й отримує введення, не змінюючи завдання."""

    def __init__(self, model, input_fn=input, output_fn=print):
        self._model = model
        self._input = input_fn
        self._output = output_fn
        # Model повідомляє про зміни; View сама читає актуальні дані.
        self._model.subscribe(self.show_tasks)

    def show_tasks(self):
        tasks = self._model.get_tasks()
        self._output("\nСписок завдань:")
        if not tasks:
            self._output("Поки що немає завдань.")
            return
        for task in tasks:
            mark = "x" if task.completed else " "
            self._output(f"{task.task_id}. [{mark}] {task.title}")

    def show_menu(self):
        self._output("\n1 — Додати завдання")
        self._output("2 — Змінити статус виконання")
        self._output("3 — Видалити завдання")
        self._output("4 — Показати список")
        self._output("0 — Вийти")

    def ask(self, prompt):
        return self._input(prompt)

    def show_message(self, message):
        self._output(message)


class TaskController:
    """Controller: обробляє дії користувача і викликає операції Model."""

    def __init__(self, model, view):
        self._model = model
        self._view = view

    def _read_task_id(self):
        try:
            return int(self._view.ask("Номер завдання: "))
        except ValueError:
            raise ValueError("Введіть цілий номер завдання.") from None

    def handle_action(self, choice):
        try:
            if choice == "1":
                title = self._view.ask("Назва завдання: ")
                self._model.add_task(title)
                self._view.show_message("Завдання додано.")
            elif choice == "2":
                self._model.toggle_task(self._read_task_id())
                self._view.show_message("Статус змінено.")
            elif choice == "3":
                self._model.delete_task(self._read_task_id())
                self._view.show_message("Завдання видалено.")
            elif choice == "4":
                self._view.show_tasks()
            elif choice == "0":
                self._view.show_message("Роботу завершено.")
                return False
            else:
                self._view.show_message("Оберіть дію від 0 до 4.")
        except ValueError as error:
            self._view.show_message(f"Помилка: {error}")
        return True

    def run(self):
        self._view.show_message("Список завдань — приклад MVC")
        self._view.show_tasks()
        try:
            while True:
                self._view.show_menu()
                choice = self._view.ask("Ваш вибір: ").strip()
                if not self.handle_action(choice):
                    break
        except (EOFError, KeyboardInterrupt):
            self._view.show_message("\nРоботу завершено.")


def run_demo():
    # Та сама модель, View і Controller; замінено лише джерело введення.
    answers = iter(("Вивчити MVC", "Завантажити код на GitHub", "1", "2"))
    model = TaskModel()
    view = TaskView(model, input_fn=lambda prompt: next(answers))
    controller = TaskController(model, view)
    view.show_message("Демонстрація MVC")
    view.show_tasks()
    for action in ("1", "1", "2", "3", "0"):
        controller.handle_action(action)


def main():
    parser = argparse.ArgumentParser(description="Навчальний приклад MVC: список завдань")
    parser.add_argument("--demo", action="store_true", help="виконати демонстрацію без введення")
    args = parser.parse_args()
    if args.demo:
        run_demo()
    else:
        model = TaskModel()
        view = TaskView(model)
        controller = TaskController(model, view)
        controller.run()


if __name__ == "__main__":
    main()
