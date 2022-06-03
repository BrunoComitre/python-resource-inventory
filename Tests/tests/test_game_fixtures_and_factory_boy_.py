from code_board.app import Column, Task
from faker import Faker
from pytest import mark

"""
pytest -m board -v

Fixtures: É basicamente uma forma de evitar repetição de código em testes.
"""

fake = Faker()

@mark.board
def test_there_must_not_be_a_column_in_the_board(board) -> None:
    assert len(board.columns) == 0

@mark.board
def test_when_inserting_a_column_you_must_actually_insert_a_column(board) -> None:
    board.insert_column(Column(name = "TO DO"))
    assert len(board.columns) == 1

@mark.board
def test_when_inserting_a_column_to_be_made_it_must_be_on_the_board(board) -> None:
    board.insert_column(Column(name = "TO DO"))
    assert str(board.columns[0]) == "TO DO"

@mark.board
def test_column_must_have_a_name() -> None:
    assert Column(name = "DOING").name == "DOING"

@mark.board
def test_when_insert_an_assignment_into_the_board_it_must_be_in_the_first_column(board_with_column) -> None:
    board_with_column.insert_task(Task(name = "Create a new task"))
    assert len(board_with_column.columns[0].task_list) == 1

@mark.board
def test_when_moving_the_card_it_should_go_to_the_next_column(board_with_columns) -> None:
    task = Task(name = fake.pystr())
    board_with_columns.insert_task(task)

    board_with_columns.moved_task(task)

    assert task in board_with_columns.columns[1]

@mark.board
def test_when_moving_the_card_it_should_remove_from_previous_column(board_with_columns) -> None:
    task = Task(name = fake.pystr())
    board_with_columns.insert_task(task)

    board_with_columns.moved_task(task)

    assert task not in board_with_columns.columns[0]

@mark.board
def test_factory_boy_exemple(factory_boy_test) -> None:
    ...

@mark.board
@mark.parametrize(
    'parametrized_board',[[1]], indirect=True)
def test_passing_parameters_to_fixture(parametrized_board) -> None:
    ...
