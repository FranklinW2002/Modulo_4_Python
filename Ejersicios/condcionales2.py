import random

aleatorio1 = random.randint(1,9)
aleatorio2 = random.randint(1,9)

if aleatorio1 == 4: 
    print("Te ganaste un chupete")
elif aleatorio1== 8:
    print("Te aganaste un balon")
elif aleatorio1 == 3 and aleatorio2 == 7 :
    print("Te ganaste un televicion")
else:
    print("Perdiste")