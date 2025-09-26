
numero_secreto = 7
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (entre 1 y 10): "))

    if intento == numero_secreto:
        print("¡Correcto! Has adivinado el número.")
        adivinado = True
    else:
        if intento > numero_secreto:
            print("Muy alto.")
        else:
            print("Muy bajo.")
