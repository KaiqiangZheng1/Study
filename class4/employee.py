class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
    
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department
    
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Department: {self.department}"
    
class Developer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language

    def get_info(self):
        return f"{super().get_info()} - Developer in {self.programming_language}"