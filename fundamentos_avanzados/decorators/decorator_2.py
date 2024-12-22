def check_access(func):
    def wrapper(employee):
        #comprobar el rol 'admin'
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            print('Acceso denegado. solo para admin')
    return wrapper


@check_access
def delete_employee(employee):
    print(f"l empleado {employee['name']} a sido eliminado")


admin = {
    'name' : 'carlos',
    'role' : 'admin',
}

employee = {'name': 'ana', 'role': 'employee'}

#delete_employee(admin)
delete_employee(employee)
