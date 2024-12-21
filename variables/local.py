x = 100

def local_function():
    x = 10
    print(f'El valor de la variable es {x}')

def show_global():
    print(f'El valor de la variable global es {x}')


show_global()
print(x)