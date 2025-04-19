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

    def take_test(self, teachers, subject=None, difficulty="medium", **kwargs):
        teacher_names = ", ".join([t.name for t in teachers])
        print(f"\nTest starting for student {self.name} under the supervision of: {teacher_names}")
        print(f"Subject: {subject} | Difficulty: {difficulty}")
        
        if kwargs:
            print("Additional Info:")
            for key, value in kwargs.items():
                print(f"  - {key}: {value}")
        
        time.sleep(3)
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
    
    def supervise_test(self, student, other_teachers=[], subject=None, difficulty="medium", **kwargs):
        # 把当前老师和其他老师组成一个老师列表
        all_teachers = [self] + other_teachers
        print(f"Teachers {[t.name for t in all_teachers]} are supervising {student.name}'s test.")
        return student.take_test(all_teachers, subject=subject, difficulty=difficulty, **kwargs)



