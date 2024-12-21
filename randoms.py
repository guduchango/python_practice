import random

# generar un numero entero aleatorio
random_number = random.randint(1,10)
print(random_number)

# elegir colores aleatorios
colors = ['rojo','azul','verde']
random_color = random.choice(colors)
print(random_color)

# barajar una lista de cartas
cards = ['as','rey','reina','jota','10']
random.shuffle(cards)
print(cards)