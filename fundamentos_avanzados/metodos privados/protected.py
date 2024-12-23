class BaseClass:
    def __init__(self): 
        self._protected_variable = 'Protected'
        self.__private_variable = 'Privated'

    def _protected_method(self):
        print('Este es un metodo protegido')


    def __private_method(self):
        print('Esto es un metodo privado')

    def public_method (self):
        self.__private_method()

base = BaseClass()
#print(base._protected_variable)
#base._protected_method()

#base.public_method()
print(base.__private_variable)

