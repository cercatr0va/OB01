class Task:
    """Класс, представляющий задачу с атрибутами."""

    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Не выполнена"  # Статус задачи по умолчанию - не выполнена

    def mark_as_done(self):
        """Отмечает задачу как выполненную."""
        self.status = "Выполнена"

    def __str__(self):
        """Возвращает строковое представление задачи."""
        return f"Название: {self.title}\nОписание: {self.description}\nСрок: {self.due_date}\nСтатус: {self.status}"


class TaskManager:
    """Класс для управления задачами."""

    def __init__(self):
        self.tasks = []  # Список задач

    def add_task(self, task):
        """Добавляет задачу в список невыполненных задач."""
        self.tasks.append(task)
        print(f"Задача '{task.title}' успешно добавлена!")

    def display_tasks(self):
        """Отображает список всех задач."""
        if not self.tasks:
            print("Список задач пуст.")
        else:
            print("Список задач:")
            for index, task in enumerate(self.tasks, 1):
                print(f"\nЗадача {index}:\n{task}")

    def mark_task_as_done(self, index):
        """Отмечает задачу как выполненную по индексу."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_done()
            print(f"Задача '{self.tasks[index].title}' отмечена как выполненная!")
        else:
            print("Неверный индекс задачи.")

    def delete_task(self, index):
        """Удаляет задачу из списка по индексу."""
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Задача '{removed_task.title}' была успешно удалена!")
        else:
            print("Неверный индекс задачи.")


def menu():
    """Функция отображения меню для работы с задачами."""
    manager = TaskManager()

    while True:
        print("\nМенеджер задач:")
        print("1. Создать задачу")
        print("2. Отобразить список задач")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            due_date = input("Введите срок выполнения задачи: ")
            task = Task(title, description, due_date)
            manager.add_task(task)
        elif choice == "2":
            manager.display_tasks()
        elif choice == "3":
            manager.display_tasks()
            index = int(input("Введите номер задачи для отметки как выполненной: ")) - 1
            manager.mark_task_as_done(index)
        elif choice == "4":
            manager.display_tasks()
            index = int(input("Введите номер задачи для удаления: ")) - 1
            manager.delete_task(index)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    menu()
