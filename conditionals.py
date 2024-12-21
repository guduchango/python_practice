x = 3

if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual que 5")
else:
    print("x es menor que 5")

print("estoy afuera")

x = 15
y = 20

if x>10 and y>25:
    print("x es mayor que 10 y y es mayor que 15")
else:
    print("nose")

if x>10 or y>25:
    print("x es mayor que 10 o y es mayor que 25")

if not x>10:
    print("x no es mayor que x")


is_member = True
age = 15

if is_member:
    if age >= 15:
        print("tienes acceso ya que eres miembro y mayor o igual que 15")
    else:
        print("no tienes acceso ya que eres miembro")
else:
    print("no eres miembro y no tienes acceso")