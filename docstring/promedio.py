def calculate_avarage(numbers):
    """
    Calcular el promedio de una lista de números

    Parámetros:
    numbers (list): Una lista de números enteros o flotantes

    Retorno:
    float: El promedio de los números en la lista
    """
    return sum(numbers) / len(numbers)

# Imprimiendo el resultado de la  función
print(calculate_avarage([1,2,3,4,5]))

