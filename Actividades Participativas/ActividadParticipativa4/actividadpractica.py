class Student:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
        self.grades: list = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        average = 0
        for j in self.grades:
            average += j
        average /= len(self.grades)
        return average

