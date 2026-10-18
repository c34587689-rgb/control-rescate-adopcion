
from animales import registrar_animal, listar_animales
from adopciones import registrar_adopcion


def mostrar_menu():
    print("\n===================================")
    print(" SISTEMA DE RESCATE Y ADOPCION ANIMAL")
    print("===================================")
    print("1. Registrar animal rescatado")
    print("2. Mostrar animales registrados")
    print("3. Registrar adopcion")
    print("4. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_animal()
        elif opcion == "2":
            listar_animales()
        elif opcion == "3":
            registrar_adopcion()
        elif opcion == "4":
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    main()
