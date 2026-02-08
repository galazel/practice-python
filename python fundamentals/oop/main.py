class Person:

    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary <= 0:
            raise ValueError("Salary cannot be less than 0")
        self.__salary = new_salary