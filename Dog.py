from Animal import Animal


class Dog(Animal):
    def __init__(self, hair, name, color, age, sex):
        super().__init__(name, color, age, sex)
        self.hair = hair

    def housekeeping(self):
        print(f"{self.name}{self.age}{self.sex}{self.hair}{self.color}会看家")

    def call(self):
        print("汪汪叫")


dog = Dog('长发', '贝贝', '黑色', '10', '男')
dog.housekeeping()
