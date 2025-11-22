# Programa de notas - Prueba / Avance 1
# Calcula el promedio de UN alumno y dice si aprueba

print("=== Cálculo de promedio de un alumno ===")

nombre = input("Ingrese el nombre del alumno: ")

nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"\nAlumno: {nombre}")
print(f"Promedio: {promedio:.2f}")

if promedio >= 7:
    print("Estado: APROBADO")
else:
    print("Estado: DESAPROBADO")
