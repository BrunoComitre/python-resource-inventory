from dataclasses import dataclass


@dataclass
class Task:
    name: str


class Column:
    def __init__(self, name,task_list=None):
        self.name = name
        self.task_list = task_list or []

    def insert_task(self, task):
        self.task_list.append(task)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self) -> str:
        return f'Tasks(name="s{self.name}", task_list ={self.task_list})'

    def __getitem__(self, index):
        return self.task_list[index]

    def remove_task(self, task):
        self.task_list.remove(task)

class Board:
    def __init__(self, columns=None):
        self.columns = columns or []

    def insert_column(self, column) -> None:
        self.columns.append(column)

    def insert_task(self, task) -> None:
        self.columns[0].insert_task(task)

    def __repr__(self) -> str:
        return f'Board(columns ={self.columns})'

    def moved_task(self, task) -> None:
        if task in self.columns[0]:
            self.columns[0].remove_task(task)
            self.columns[1].insert_task(task)
