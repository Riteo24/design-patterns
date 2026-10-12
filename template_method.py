"""Шаблонний метод: незмінний порядок кроків із різним форматуванням звіту."""
from abc import ABC, abstractmethod
from html import escape


class ReportGenerator(ABC):
    def generate(self, rows):
        # Шаблон алгоритму спільний для всіх звітів.
        data = self.prepare_data(rows)
        body = self.format_data(data)
        return self.wrap_report(body)

    def prepare_data(self, rows):
        return [str(row).strip() for row in rows if str(row).strip()]

    @abstractmethod
    def format_data(self, rows):
        pass

    def wrap_report(self, body):
        return body


class TextReport(ReportGenerator):
    def format_data(self, rows):
        return "\n".join(rows)

    def wrap_report(self, body):
        return "Текстовий звіт:\n" + body


class HtmlReport(ReportGenerator):
    def format_data(self, rows):
        return "".join(f"<li>{escape(row)}</li>" for row in rows)

    def wrap_report(self, body):
        return f"<ul>{body}</ul>"


def main():
    rows = [" Замовлення 1 ", "", "Замовлення 2"]
    print(TextReport().generate(rows))
    print(HtmlReport().generate(rows))


if __name__ == "__main__":
    main()
