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


teacher1 = Teacher("Mr. Li", 40, "Math")
teacher2 = Teacher("Ms. Zhang", 35, "Science")
teacher3 = Teacher("Dr. Wang", 50, "English")

student1 = Student("Xiao Ming", 16, 11)

# 老师1发起监考，同时有另外两个老师一起参与，还加了一些附加参数
teacher1.supervise_test(
    student1,
    other_teachers=[teacher2, teacher3],
    subject="Final Exam",
    difficulty="hard",
    room="305A",
    duration="90 mins"
)



# Testing the new test-taking functionality
# teacher1.supervise_test(student1)  # This will trigger the 3-second test duration
# teacher2.supervise_test(student2)

# would = teacher2.supervise_test(student2)
# print(would)