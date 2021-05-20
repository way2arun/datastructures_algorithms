class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@noemail.com'
        Employee.num_of_emps += 1

    def __repr__(self):
        return f'Employee ({self.first}, {self.last}, {self.pay})'

    def __str__(self):
        return f'Employee ({self.first}, {self.last}, {self.pay})'

    def fullname(self):
        return f'{self.first} {self.last}'

    def raise_amounts(self):
        return int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_employee(self, emp):
        if emp  in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print(f'--> {emp.fullname()}')

emp1 = Employee("abce", "xyz", 5000)
emp2 = Employee("aaa", "bbb", 6000)

print(emp1)
print(emp2)
print(repr(emp1))
print(str(emp1))
print(emp1.email)
print(emp2.email)
print(emp1.fullname())
print(emp1.pay)
print(Employee.fullname(emp2))

Employee.set_raise_amt(1.05)
emp1.raise_amount = 1.10
print(emp1.raise_amounts())
emp2.raise_amount = 1.02
print(emp2.raise_amounts())
print(Employee.raise_amount)


print(Employee.__dict__)
print(emp1.__dict__)

print(Employee.num_of_emps)
emp1_str = 'John-Doe-7000'
new_emp1 = Employee.from_string(emp1_str)

print(new_emp1.pay)
print(new_emp1.email)

dev_1 = Developer("abce", "xyz", 5000, "java")
print(dev_1.email)
print(dev_1.raise_amount)
print(dev_1.prog_lang)
dev_2 = Developer("abced", "xyzd", 5000, "python")
manager_1 = Manager('a', 'b', 9000, [dev_1])
print(manager_1.email)
manager_1.print_employees()
manager_1.add_employee(dev_2)
manager_1.print_employees()
manager_1.remove_employee(dev_1)
manager_1.print_employees()




