import multiprocessing

#funcion que calculo el cuadrado de un numero
def calculate_square(n):
    return n*n

if __name__=='__main__':
    numbers = [1,2,3,4,5]

    #crear un pool
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_square,numbers)

    print(f'resultados: {results}')