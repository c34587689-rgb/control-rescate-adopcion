
from animales import animales


def registrar_adopcion():
    print("\n--- REGISTRAR ADOPCION ---")

    disponibles = [
        animal for animal in animales
        if not animal["adoptado"]
    ]

    if not disponibles:
        print("No hay animales disponibles para adopcion.")
        return

    print("\nAnimales disponibles:")

    for animal in disponibles:
        print(
            f"ID: {animal['id']} | "
            f"Nombre: {animal['nombre']} | "
            f"Especie: {animal['especie']}"
        )

    try:
        animal_id = int(input("\nIngrese el ID del animal: "))
    except ValueError:
        print("Error: debe ingresar un numero.")
        return

    animal_elegido = next(
        (animal for animal in disponibles
         if animal["id"] == animal_id),
        None
    )

    if animal_elegido is None:
        print("ID incorrecto o animal no disponible.")
        return

    adoptante = input("Nombre del adoptante: ").strip()

    if not adoptante:
        print("El nombre del adoptante es obligatorio.")
        return

    animal_elegido["adoptado"] = True
    animal_elegido["adoptante"] = adoptante

    print(
        f"\nAdopcion registrada correctamente. "
        f"{animal_elegido['nombre']} fue adoptado por {adoptante}."
    )
