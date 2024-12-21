# iterar en cadenas

text = "hola mundo"
iter_text= iter(text)

for char in iter_text:
    print(char)

# iterador numeros impares

limit = 10
odd_itter = iter(range(1,limit+1,2))

for num in odd_itter:
    print(num)


def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

#fibonacci
# 0 1 1 2 3 5 8 13 21

def fibonacci(limit):
    a, b = 0,1

    while a < limit:
        yield a
        a, b = b, a+b

for num in fibonacci(50):
    print(num)
