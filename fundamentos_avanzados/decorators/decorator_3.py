
 # Decorador que comprueba si un empleado tiene un rol especifico
def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            #si el rol del empleado coincide con el rol requerido
            if employee.get('role') == required_role:
                return func(employee)
            else:
                print(f'acceso denegado. Solo {required_role} pueden realizar esta accion')

        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f"registrando accion para el empleado {employee['name']}")
        return func(employee)
    return wrapper


@check_access('admin')
@log_action
def delete_employee(employee):
    print(f"el empleado {employee['name']}, a sido eliminado")


admin = {
    'name' : 'carlos',
    'role' : 'admin',
}

employee = {'name': 'ana', 'role': 'employee'}

delete_employee(admin)
#delete_employee(employee)

