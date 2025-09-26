
saldo = 500  # Saldo inicial

while True:
    print(f"\nSaldo disponible: ${saldo}")
    monto = int(input("Ingrese el monto a retirar (o 0 para salir): "))

    if monto == 0:
        print("Gracias por usar el cajero. ¡Hasta luego!")
        break
    elif monto < 0:
        print("Monto inválido. Debe ser mayor que cero.")
    elif monto > saldo:
        print("Fondos insuficientes.")
    elif monto % 10 != 0:
        print("El monto debe ser múltiplo de 10.")
    else:
        saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
