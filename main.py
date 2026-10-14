from datetime import datetime


FORMATO_FECHA = "%d/%m/%Y"


def pedir_texto(mensaje):
    while True:
        valor =(input(mensaje)).strip()
        if valor:
            return valor
        print("Este dato no puede quedar vacío. Inténtalo de nuevo.")


def pedir_fecha(mensaje):
    while True:
        valor = input(mensaje).strip()
        try:
            fecha = datetime.strptime(valor, FORMATO_FECHA)
            return fecha.strftime(FORMATO_FECHA)
        except ValueError:
            print("Fecha no válida. Usa el formato DD/MM/AAAA (por ejemplo, 25/12/2026).")


def crear_tarea():
    print("\n--- Nueva tarea ---")
    titulo = pedir_texto("Título: ")
    descripcion = pedir_texto("Descripción: ")
    materia = pedir_texto("Materia: ")
    fecha = pedir_fecha("Fecha de entrega (DD/MM/AAAA): ")

    tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "materia": materia,
        "fecha": fecha,
    }
    return tarea


def mostrar_tareas(tareas):
    print("\n--- Tareas registradas ---")
    if not tareas:
        print("No hay tareas registradas todavía.")
        return

    for numero, tarea in enumerate(tareas, start=1):
        print(f"\nTarea {numero}")
        print(f"  Título:      {tarea['titulo']}")
        print(f"  Descripción: {tarea['descripcion']}")
        print(f"  Materia:     {tarea['materia']}")
        print(f"  Entrega:     {tarea['fecha']}")


def mostrar_menu():
    print("\n=== Organizador Académico ===")
    print("1. Crear tarea")
    print("2. Mostrar tareas")
    print("3. Salir")


def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            tareas.append(crear_tarea())
            print("Tarea añadida correctamente.")
        elif opcion == "2":
            mostrar_tareas(tareas)
        elif opcion == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Elige 1, 2 o 3.")


if __name__ == "__main__":
    main()
