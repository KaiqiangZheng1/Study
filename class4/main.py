from employee import Manager, Developer
from benefits import ManagerBenefits, DeveloperBenefits

# Creating instances
manager1 = Manager("Alice", 35, 80000, "HR")
developer1 = Developer("Bob", 28, 70000, "Python")
manager2 = Manager("Charlie", 40, 90000, "Finance")
developer2 = Developer("David", 30, 75000, "JavaScript")

manager_benefits = ManagerBenefits()
developer_benefits = DeveloperBenefits()

# Using polymorphism with a loop
employees = [manager1, developer1, manager2, developer2]
benefits = [manager_benefits, developer_benefits]

print("\n--- Employee Information ---")
for emp in employees:
    print(emp.get_info())

print("\n--- Employee Benefits ---")
for benefit in benefits:
    print(", ".join(benefit.get_benefits()))
