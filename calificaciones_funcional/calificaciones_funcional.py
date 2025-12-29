from functools import reduce

estudiantes = ("Ana", "Luis", "Carlos", "María", "José")
notas = (85, 42, 78, 91, 60)

estado = lambda n: "Aprobado" if n >= 70 else "Reprobado"

registro = tuple(zip(
    estudiantes,
    notas,
    map(estado, notas)
))

promedio = reduce(lambda a, b: a + b, notas) / len(notas)

print(registro)
print(promedio)
