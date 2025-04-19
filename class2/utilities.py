#(Helper functions for school operations)  utils.py

def welcome_message():
    return "Welcome to our School Management System!"

def print_person_details(person):
    print(person.introduce())  # Polymorphism: Works for any Person, Student, or Teacher
