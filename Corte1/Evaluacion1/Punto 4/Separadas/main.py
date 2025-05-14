from cajero import Cajero, mostrar_menu, obtener_monto

def main():
    cajero = Cajero()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            print(f"Tu saldo actual es: ${cajero.ver_saldo():,.2f}")
        elif opcion == '2':
            try:
                monto = obtener_monto()
                nuevo_saldo = cajero.ingresar(monto)
                print(f"Has ingresado ${monto:,.2f}. Saldo actual: ${nuevo_saldo:,.2f}")
            except ValueError as e:
                print("Error:", e)
        elif opcion == '3':
            try:
                monto = obtener_monto()
                nuevo_saldo = cajero.retirar(monto)
                print(f"Has retirado ${monto:,.2f}. Saldo actual: ${nuevo_saldo:,.2f}")
            except ValueError as e:
                print("Error:", e)
        elif opcion == '4':
            print("Gracias por usar el cajero. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción del 1 al 4.")

if __name__ == "__main__":
    main()
