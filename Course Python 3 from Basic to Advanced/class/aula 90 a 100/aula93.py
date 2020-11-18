class People:
    year_atual = 2020
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def get_year_birthday(self):
        print(self.year_atual - self.age)
    
    @classmethod
    def for_year_birthday(cls, name, year_birthday):
        age = cls.year_atual - year_birthday
        return cls(name, age)


people = People("joão",32)
print(people.age)
people.get_year_birthday()

people = People.for_year_birthday("Carlos",1990)
print(people.age)
people.get_year_birthday()
