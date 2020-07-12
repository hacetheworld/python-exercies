class Person:
    def __init__(self, first, last, age):
        self.name = first
        self.last = last
        self.age = age

    def greet(self):
        print(self.name, self.last, self.age)


user1 = Person("Ajay", "Meena", 20)
user1.greet()
print(user1)
