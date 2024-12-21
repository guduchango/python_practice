def greet(name, lastname = "ponce"):
    print("hola mundo",name, lastname)

greet("carli","orozco")
greet("diego")


def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def calculator():
    while True:
        print("seleccione una operacion")
        print("1. Suma")
        print("2. Resta")
        print("3. División")
        print("4. Multiplicación")
        print("5. Salir")
        option = input("Intrese su opción(1,2,3,4,5): ")

        if option == 5:
            print("saliendo de la calculadora")
            break
        
        if option in ["1","2","3","4"]:
            num1 = float(input("Ingrese el primer numero"))
            num2 = float(input("Ingrese el segundo numero"))

            if option == "1":
                print("la suma es:", add(num1,num2))
            elif option == "2":
                print("la resta es:", substract(num1,num2))
            elif option == "3":
                print("la division es:", divide(num1,num2))
            elif option == "3":
                print("la multiplicacion es:", multiply(num1,num2))
        else:
            print("Opcion no vlaida, por favor intenta de nuevo")

calculator()



        

