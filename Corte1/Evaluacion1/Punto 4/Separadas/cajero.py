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
