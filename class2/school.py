import random
import time

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


class Student(Person):  # Inherits from Person
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        self.test_scores = []

    def introduce(self):  # Overriding the method
        return f"Hi, I'm {self.name}, {self.age} years old, and I'm in grade {self.grade}."
    
    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, grade={self.grade})"

    def take_test(self, teacher):
        print(f"\nTest starting for student {self.name} under {teacher.name}'s supervision...")
        time.sleep(3)  # Simulating test duration of 3 seconds
        score = random.randint(60, 100)
        self.test_scores.append(score)
        print(f"Test completed! {self.name} scored: {score}")
        return score


class Teacher(Person):  # Inherits from Person
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):  # Overriding the method
        return f"Hello, I'm {self.name}, a {self.age}-year-old teacher, and I teach {self.subject}."
    
    def supervise_test(self, student):
        print(f"Teacher {self.name} is supervising {student.name}'s test in {self.subject}")
        return student.take_test(self)


