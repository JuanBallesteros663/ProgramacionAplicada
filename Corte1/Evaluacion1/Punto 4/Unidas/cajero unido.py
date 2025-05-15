class Cajero:
    def __init__(self, saldo_inicial=5000000):
        self.saldo = saldo_inicial
        print(f"Cajero iniciado con saldo de ${self.saldo:,}")

    def ver_saldo(self):
        return self.saldo

    def ingresar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a ingresar debe ser mayor que cero.")
        self.saldo += monto
        return self.saldo

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor que cero.")
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        self.saldo -= monto
        return self.saldo

def mostrar_menu():
    print("\n======= CAJERO AUTOMÁTICO =======")
    print("1. Ver saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

def obtener_monto():
    while True:
        try:
            monto = float(input("Ingrese el monto: "))
            return monto
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")

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
