# Programa de notas - Prueba / Avance 3
# Varios alumnos + estadísticas simples del curso

print("=== Carga de notas de varios alumnos ===")

cantidad = int(input("¿Cuántos alumnos desea cargar?: "))

nombres = []
promedios = []
estados = []

for i in range(cantidad):
    print(f"\nAlumno {i + 1} de {cantidad}")
    nombre = input("Nombre: ")

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 7:
        estado = "APROBADO"
    else:
        estado = "DESAPROBADO"

    nombres.append(nombre)
    promedios.append(promedio)
    estados.append(estado)

print("\n=== Resultados por alumno ===")
for i in range(cantidad):
    print(f"{nombres[i]} - Promedio: {promedios[i]:.2f} - {estados[i]}")

# --- estadísticas ---
aprobados = 0
suma_promedios = 0
mejor_promedio = promedios[0]
mejor_alumno = nombres[0]

for i in range(cantidad):
    # contar aprobados
    if promedios[i] >= 7:
        aprobados += 1

    # acumular para promedio general
    suma_promedios += promedios[i]

    # buscar mejor promedio
    if promedios[i] > mejor_promedio:
        mejor_promedio = promedios[i]
        mejor_alumno = nombres[i]

desaprobados = cantidad - aprobados
promedio_general = suma_promedios / cantidad

print("\n=== Estadísticas del curso ===")
print(f"Cantidad de alumnos: {cantidad}")
print(f"Aprobados: {aprobados}")
print(f"Desaprobados: {desaprobados}")
print(f"Mejor promedio: {mejor_promedio:.2f} (Alumno: {mejor_alumno})")
print(f"Promedio general del curso: {promedio_general:.2f}")
