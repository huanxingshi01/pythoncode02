from Animal import Animal


class Cat(Animal):
    def __init__(self, hair, name, color, age, sex):
        super().__init__(name, color, age, sex)
        self.hair = hair

    def grab(self):
        print(f"{self.hair}{self.color}{self.name}{self.age}{self.sex}会捉老鼠")

    def call(self):
        print("喵喵叫")


cat = Cat('短发', '咪咪', '黑色', '10', '男')
cat.grab()