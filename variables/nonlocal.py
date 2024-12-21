def outer_function():
    x = 'enclosing'
    def inner_function():
        nonlocal x
        x = 'modified'
        print(f'el valor n inner es: {x}')

    inner_function()
    print(f'El valor de esta variable es {x}')

outer_function()