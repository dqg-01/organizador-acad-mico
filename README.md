# Organizador Académico

Aplicación de consola desarrollada en Python para organizar las tareas escolares de un estudiante.

## Objetivo

Desarrollar una aplicación que permita organizar las tareas escolares de un estudiante, agrupándolas por materia y fecha de entrega.

## Tecnologías

* Python 3.14.7
* Git
* GitHub
* OpenCode

## Estado del proyecto

Funcional: incluye todas las funciones previstas (crear tareas, mostrarlas, buscar por materia, marcarlas como completadas y guardarlas en disco).

## Funcionalidades

1. Crear tareas con título, descripción, materia y fecha de entrega.
2. Mostrar todas las tareas registradas, con su estado (pendiente o completada).
3. Buscar tareas por materia, ignorando mayúsculas y espacios sobrantes.
4. Marcar una tarea como completada, identificándola por su número.
5. Guardar las tareas en un archivo JSON (`tareas.json`) y cargarlas automáticamente al iniciar.
6. Validar los datos: rechaza campos vacíos, fechas inexistentes y fechas anteriores al día actual.

## Requisitos

* Python 3 (probado con Python 3.14.7). No necesita dependencias externas.

## Cómo ejecutar

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta:

   ```
   python main.py
   ```

3. Usa el menú para elegir una opción escribiendo su número y pulsando Enter.

## Formato de fecha

Las fechas de entrega se escriben como `DD/MM/AAAA` (por ejemplo, `25/12/2026`).
No se aceptan fechas inexistentes (por ejemplo, `31/02/2026`) ni anteriores a hoy.

## Persistencia de datos

Las tareas se guardan en `tareas.json`, en la misma carpeta del programa, y se cargan
automáticamente al iniciarlo. Este archivo contiene datos personales de prueba, por lo que
está excluido del repositorio mediante `.gitignore`.
