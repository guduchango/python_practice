class Employee:
    def __init__(self,name,*args,**kwargs) -> None:
        self.name = name
        self.skills = args
        self.details = kwargs

    def show_employee(self):
        print(f'Employee:{self.name}')
        print('Skills',self.skills)
        print('Details', self.details)

employee = Employee('carlos','Python', 'Java','C++', age=30, city='Bogota')
employee.show_employee()