from code_board.app import Board, Column, Task
from faker import Faker
from pytest import fixture

"""
pytest -m board -v

Fixtures: É basicamente uma forma de evitar repetição de código em testes.
"""

fake = Faker()


import factory


class ColumnsFactory(factory.Factory):
    class Meta:
        model = Column

    name = factory.Faker('name')
    task_list = [Task('A')]


class BoardFactory(factory.Factory):
    class Meta:
        model = Board

    columns = ColumnsFactory.build_batch(5)


@fixture
def parametrized_board(request):
    return Board()

@fixture
def factory_boy_test():
    return BoardFactory.build()


@fixture#(scope='session')
def board():
    return Board()

@fixture
def board_with_column(board):
    board.insert_column(Column(fake.pystr()))
    return board

@fixture
def board_with_columns(board_with_column):
    board_with_column.insert_column(Column(fake.pystr()))
    board_with_column.insert_task(Task(fake.pystr()))
    return board_with_column
