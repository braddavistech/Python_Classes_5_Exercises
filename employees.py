class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = list()

    def get_company_name(self):
        """Returns the name of the company"""
        return self.company_name

    def add_employee(self, employee):
      self.employees.append(employee)
    # Add the remaining methods to fill the requirements above

    def list_employee(self):
      temp = [f'{emp.name} works at {self.company_name}, founded in {self.date_founded}. {emp.name} is a {emp.job_title} in the {emp.department}.' for emp in self.employees]
      return (" ").join(temp)

class Employee(Company):
  def __init__(self, name, job_title, department):
    self.name = name
    self.job_title = job_title
    self.department = department

  # def employee_details(self):
  #   return f'{self.name} works in the {self.department} department as a {self.job_title}.'

bdtech = Company("BD TECH", "2017")
brad = Employee("Brad Davis", "Web Developer", "New Development")
john = Employee("John Smith", "UI Designer", "New Development")
julie = Employee("Julie Maddox", "Accountant", "Finance")
brendan = Employee("Brendan", "Senior Developer", "New Development")

bdtech.add_employee(brad)
bdtech.add_employee(john)
bdtech.add_employee(julie)
# print(brad.employee_details())
bdtech.employees.append(brendan)

print(bdtech.list_employee())
