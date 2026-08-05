class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_name(self):
        print(f"Employee Name: {self.name}")

    def calculate_salary(self):
        print(f"Monthly Salary: ₹{self.salary}")


# Write toa  file
with open("notes.txt", "w") as file:
    file.write("Welcome to AI Project")

 # Read from a file 
with open("notes.txt", "r") as file:
    content = file.read()

print(content)

# Exception Handling
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")

except ValueError:
    print("Please enter a valid number.")