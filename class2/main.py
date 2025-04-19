from school import Student, Teacher
import utilities

# Print welcome message
print(utilities.welcome_message())

# Create instances of Student and Teacher
student1 = Student("Alice", 14, 9)
student2 = Student("Bob", 16, 11)
teacher1 = Teacher("Mr. Smith", 40, "Mathematics")
teacher2 = Teacher("Ms. Johnson", 35, "Science")

# Using Polymorphism: Calling `introduce()` on different objects
print(student1)  
print(student1.introduce())           # Hi, I'm Alice, 14 years old, and I'm in grade 9.
#utilities.print_person_details(student1)  # Hi, I'm Alice, 14 years old, and I'm in grade 9.
print(student2)

#utilities.print_person_details(student2)  # Hi, I'm Bob, 16 years old, and I'm in grade 11.
utilities.print_person_details(teacher1)  # Hello, I'm Mr. Smith, a 40-year-old teacher, and I teach Mathematics.


# Testing the new test-taking functionality
teacher1.supervise_test(student1)  # This will trigger the 3-second test duration
teacher2.supervise_test(student2)
 
# would = teacher2.supervise_test(student2)
# print(would)