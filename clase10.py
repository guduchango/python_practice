numbers = {1:"uno",2:"dos",3:"tres"}
print(numbers[2])
information = {"nombre": "carla", "apellido":"florida", "altura":1.6, "edad":29}
del information["edad"]
print(information)
claves = information.keys()
print(claves)
valores = information.values()
print(valores) 
pairs = information.items()
print(pairs)
contacts = {
    'carla':{'apellido': 'florida', 'altura': 1.6},
    'diego': {'apellido': 'ponce', 'altura': 1.8}
}
print(contacts["carla"])