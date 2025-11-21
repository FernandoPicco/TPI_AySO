
# Programa de notas - Prueba 3: Calcula el promedio de varios alumnos, estadísticas simples y posibilidad de repetir carga.

print("****Programa de notas de alumnos****")

while True:    

    # Pedir cantidad de alumnos

    cantidad_alumnos = int(input("¿Cuántos alumnos deses cargar?: "))

    # Listas para guardar datos
    nombres = []
    promedios = []

    aprobados = 0
    desaprobados = 0

    # Cargar alumnos con un ciclo for
    for i in range(cantidad_alumnos):
        print("Alumno", i+1)
    
        nombre = input("Nombre: ").strip()
        nota_1 = float(input("Nota 1: "))
        nota_2 = float(input("Nota 2: "))
        nota_3 = float(input("Nota 3: "))

        promedio = (nota_1 + nota_2 + nota_3) / 3
    
        nombres.append(nombre)
        promedios.append(promedio)

    # Vr si aprueba

        if promedio >= 7:
            aprobados += 1
            estado = "Aprobado"
        else:
            desaprobados += 1
            estado = "Desaprobado"
    
        print(f"Promedio de {nombre}: {promedio:.2f} => {estado}")
    
    # Estadísticas finales
    print("****Resultados Generales****")
    print("Cantidad de alumnos:", cantidad_alumnos)
    print("Aprobados (>= 7):", aprobados)
    print("Desaprobados:", desaprobados)

    promedio_general = sum(promedios) / cantidad_alumnos
    print(f"Promedio general del curso: {promedio_general:.2f}")

    mejor_promedio = max(promedios)
    indice_mejor = promedios.index(mejor_promedio)
    nombre_mejor = nombres[indice_mejor]

    print(f"Mejor promedio: {nombre_mejor} con {mejor_promedio:.2f}")

    # ¿Desea repetir?
    repetir = input("¿Desea cargar otro grupo de alumnos? (s/n): ").strip().lower()
    if repetir != "s":
        print("Programa finalizado.")
        break




