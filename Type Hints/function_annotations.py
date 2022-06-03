"""
The dunder __annotations__, was created for exibes the information type hints
"""

# Example in the helping sense

def sum(x: "First value to be evaluated by the function",
        y: "Second value to be evaluated by the function"):
    return x + y

print(sum(2,3))
print(sum.__annotations__)
print()


# Annotation Syntax

def example(x:"Annotation in the simplest format",
            y: "Optional parameter annotation" = 99) -> "Function return value annotation":
    ...

print(example.__annotations__)
print()

# Example using Types

def sum_two_numbers(x: int, y:int) -> int:
    ...

print(sum_two_numbers.__annotations__)
print()

def check_json(json:dict, *parameters: list) -> bool:
    ...

print(check_json.__annotations__)
print()
