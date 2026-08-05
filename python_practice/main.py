from calculator import add,subtract,multiply,divide
from employee import Employee

employee = Employee("Jayanth", 50000)
employee.display_name()
employee.calculate_salary()

result = add(10, 20)
result1 = subtract(10, 20)
result3 = multiply(10, 20)
result43 = divide(10, 20)

print(result)
print(result1)
print(result3)
print(result43)