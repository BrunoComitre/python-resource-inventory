class A:
    example = 123


test1 = A()
test2 = A()
print(test1.example)
print(test2.example)
print(A.example)
print()

A.example = 321
test1 = A()
test2 = A()
print(test1.example)
print(test2.example)
print(A.example)
print()

test1 = A()
test1.example = 456
print(test1.__dict__)
print(test2.__dict__)
print(A.__dict__)
print(test1.example)
print(A.example)
print()

class B:
    example = 123
    
    def __init__(self) -> None:
        pass

B.example = "Alterado"

test1 = B()
test2 = B()
print(test1.example)
print(test2.example)
print(B.example)
print()


class C:
    example = 123
    
    def __init__(self) -> None:
        self.example = 789


test1 = C()
test2 = C()
print(test1.example)
print(test2.example)
print(C.example)
print()