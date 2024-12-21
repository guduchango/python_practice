
# Leer un archivo linea por linea
"""with open('caperusita.txt','r') as file:
    for lineas in file:
        print(lineas.strip())"""

# Leer todas las lineas en una lista
# with open('caperusita.txt','r') as file:
#     lines = file.readlines()
#     print(lines)

# añadir texto
"""with open('caperusita.txt','a') as file:
    file.write("\n\nBy:ChatGPT")"""

#Sobreescribir el texto
with open('caperusita.txt','w') as file:
    file.write("\n\nBy:chatGTP")