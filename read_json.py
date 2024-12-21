import json

# lectura del archivo
with open('products.json', mode='r') as file:
    products = json.load(file)

# mostrar el contenido
for product in products:
    #print(product)
    print(f"Product:{product['name']}, Price: {product['price']}")
