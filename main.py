import json
from datetime import datetime

FORMATO_FECHA = "%d/%m/%Y"
ARCHIVO_DATOS = "tareas.json"


def pedir_texto(mensaje):
    while True:
        valor = (input(mensaje)).strip()
        if valor:
            return valor
        print("Este dato no puede quedar vacío. Inténtalo de nuevo.")


def pedir_fecha(mensaje):
    while True:
        valor = input(mensaje).strip()
        try:
            fecha = datetime.strptime(valor, FORMATO_FECHA)
        except ValueError:
            print("Fecha no válida. Usa el formato DD/MM/AAAA (por ejemplo, 25/12/2026).")
            continue

        if fecha.date() < datetime.today().date():
            print("La fecha de entrega no puede ser anterior a hoy.")
            continue

        return fecha.strftime(FORMATO_FECHA)


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
        "completada": False,
    }
    return tarea


def mostrar_tareas(tareas):
    print("\n--- Tareas registradas ---")
    if not tareas:
        print("No hay tareas registradas todavía.")
        return

    for numero, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea.get("completada") else "Pendiente"
        print(f"\nTarea {numero}")
        print(f"  Título:      {tarea['titulo']}")
        print(f"  Descripción: {tarea['descripcion']}")
        print(f"  Materia:     {tarea['materia']}")
        print(f"  Entrega:     {tarea['fecha']}")
        print(f"  Estado:      {estado}")


def filtrar_por_materia(tareas, materia):
    materia = materia.strip().lower()
    return [
        tarea for tarea in tareas
        if tarea["materia"].strip().lower() == materia
    ]


def marcar_completada(tareas):
    if not tareas:
        print("\nNo hay tareas registradas todavía.")
        return False

    mostrar_tareas(tareas)
    valor = input("\nNúmero de la tarea a marcar como completada: ").strip()
    if not valor.isdigit():
        print("Debes escribir un número válido.")
        return False

    numero = int(valor)
    if numero < 1 or numero > len(tareas):
        print(f"El número debe estar entre 1 y {len(tareas)}.")
        return False

    tarea = tareas[numero - 1]
    if tarea.get("completada"):
        print("Esa tarea ya estaba completada.")
        return False

    tarea["completada"] = True
    print(f'Tarea {numero} ("{tarea["titulo"]}") marcada como completada.')
    return True


def guardar_tareas(tareas):
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            json.dump(tareas, archivo, ensure_ascii=False, indent=2)
    except OSError as error:
        print(f"No se pudieron guardar las tareas: {error}")


def cargar_tareas():
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except (OSError, json.JSONDecodeError) as error:
        print(f"No se pudieron cargar las tareas guardadas: {error}")
        return []


def mostrar_menu():
    print("\n=== Organizador Académico ===")
    print("1. Crear tarea")
    print("2. Mostrar tareas")
    print("3. Buscar por materia")
    print("4. Marcar tarea como completada")
    print("5. Salir")


def main():
    tareas = cargar_tareas()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            tareas.append(crear_tarea())
            guardar_tareas(tareas)
            print("Tarea añadida correctamente.")
        elif opcion == "2":
            mostrar_tareas(tareas)
        elif opcion == "3":
            if not tareas:
                print("\nNo hay tareas registradas todavía.")
            else:
                materia = pedir_texto("Materia a buscar: ")
                encontradas = filtrar_por_materia(tareas, materia)
                if encontradas:
                    mostrar_tareas(encontradas)
                else:
                    print(f'\nNo se encontraron tareas para la materia "{materia}".')
        elif opcion == "4":
            if marcar_completada(tareas):
                guardar_tareas(tareas)
        elif opcion == "5":
            guardar_tareas(tareas)
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Elige 1, 2, 3, 4 o 5.")


if __name__ == "__main__":
    main()
