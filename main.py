class car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def accelerate(self, n):
        self.speed = self.speed + n
        print(f'{self.brand} разгонятся до: {self.speed} ')
Car = car('BMW', 60)
Car.accelerate(30)
# Это мой проект менеджер задач