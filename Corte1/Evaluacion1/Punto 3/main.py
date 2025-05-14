from calculadora import Calculadora, mostrar_menu, ejecutar_operacion

def main():
    calculadora = Calculadora()
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '5':
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break
        else:
            ejecutar_operacion(calculadora, opcion)

if __name__ == "__main__":
    main()
