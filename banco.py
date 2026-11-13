def cajero_automatico():
    PIN_CORRECTO = "1234"
    saldo = 500.0
    intentos = 3

    print("=== SIMULADOR DE CAJERO AUTOMÁTICO ===")

    while intentos > 0:
        pin = input("Ingrese su PIN de 4 dígitos: ")
        if pin == PIN_CORRECTO:
            print("\n¡Acceso concedido!")
            print(f"Saldo actual: ${saldo:.2f}")

            try:
                monto = float(input("Monto a retirar: $"))
                if monto <= 0:
                    print("Error: El monto debe ser mayor a 0.")
                elif monto > saldo:
                    print("Error: Saldo insuficiente.")
                elif monto % 10 != 0:
                    print("Error: El cajero solo entrega billetes múltiplos de $10.")
                else:
                    saldo -= monto
                    print(
                        f"\nRetiro exitoso. Retiraste: ${monto:.2f}"
                    )
                    print(f"Nuevo saldo: ${saldo:.2f}")
            except ValueError:
                print("Error: Por favor ingrese un número válido.")
            return

        else:
            intentos -= 1
            print(f"PIN incorrecto. Intentos restantes: {intentos}\n")

    print("Tarjeta bloqueada por demasiados intentos fallidos.")


cajero_automatico()