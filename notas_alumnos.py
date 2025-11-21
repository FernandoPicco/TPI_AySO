
# Programa de notas - Pruba 1: Calcula el promedio de un alumno y dice si aprueba

print("****Cálculo de promedio de un alumno****")

nombre = input("Ingrese el nombre del alumno: ").strip()
nota_1 = float(input("Ingrese la nota 1: ").strip())
nota_2 = float(input("Ingrese la nota 2: ").strip())
nota_3 = float(input("Ingrese la nota 3: ").strip())

promedio = (nota_1 + nota_2 + nota_3) / 3

print(f"Alumno: {nombre}")
print(f"Promedio: {promedio:.2f}")

if promedio >= 7:
    print("Estado: Aprobado")

else:
    print("Estado: Desaprobado")