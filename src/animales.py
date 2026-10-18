
animales = []


def registrar_animal():
    print("\n--- REGISTRAR ANIMAL RESCATADO ---")

    nombre = input("Nombre del animal: ").strip()
    especie = input("Especie (perro, gato, etc.): ").strip()
    edad = input("Edad aproximada: ").strip()
    estado = input("Estado de salud: ").strip()

    if not nombre or not especie:
        print("El nombre y la especie son obligatorios.")
        return

    animal = {
        "id": len(animales) + 1,
        "nombre": nombre,
        "especie": especie,
        "edad": edad,
        "estado": estado,
        "adoptado": False
    }

    animales.append(animal)
    print(f"\nAnimal {nombre} registrado correctamente.")


def listar_animales():
    print("\n--- ANIMALES REGISTRADOS ---")

    if not animales:
        print("Todavia no hay animales registrados.")
        return

    for animal in animales:
        situacion = "Adoptado" if animal["adoptado"] else "Disponible"

        print(f"\nID: {animal['id']}")
        print(f"Nombre: {animal['nombre']}")
        print(f"Especie: {animal['especie']}")
        print(f"Edad: {animal['edad']}")
        print(f"Estado de salud: {animal['estado']}")
        print(f"Situacion: {situacion}")
