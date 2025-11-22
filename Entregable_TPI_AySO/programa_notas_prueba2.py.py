# Programa de notas - Prueba / Avance 2
# Carga varios alumnos, calcula promedios y estadísticas simples

print("***** Programa de notas de alumnos *****")

# 1) Pedir cantidad de alumnos
cantidad_alumnos = int(input("¿Cuántos alumnos quiere cargar?: "))

# 2) Listas para guardar datos
nombres = []
promedios = []

aprobados = 0
desaprobados = 0

# 3) Cargar alumnos con un for
for i in range(cantidad_alumnos):
    print("\nAlumno", i + 1)

    nombre = input("Nombre: ").strip()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    promedio = (nota1 + nota2 + nota3) / 3

    nombres.append(nombre)
    promedios.append(promedio)

    # 4) Ver si aprueba
    if promedio >= 7:
        aprobados += 1
        estado = "APROBADO"
    else:
        desaprobados += 1
        estado = "DESAPROBADO"

    print(f"Promedio de {nombre}: {promedio:.2f} -> {estado}")

# 5) Estadísticas finales
print("\n===== RESULTADOS GENERALES =====")

print("Cantidad de alumnos:", cantidad_alumnos)
print("Aprobados (>=7):", aprobados)
print("Desaprobados:", desaprobados)

promedio_general = sum(promedios) / cantidad_alumnos
print(f"Promedio general del curso: {promedio_general:.2f}")

mejor_promedio = max(promedios)
indice_mejor = promedios.index(mejor_promedio)
nombre_mejor = nombres[indice_mejor]

print(f"Mejor promedio: {nombre_mejor} con {mejor_promedio:.2f}")

# ¿Desea repetir?
repetir = input("¿Desea cargar otro")