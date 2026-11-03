lapices = int(input("Ingrese la cantidad de lápices: "))
cuadernos = int(input("Ingrese la cantidad de cuadernos: "))
total = lapices + cuadernos
print(f'El total es: {total}')

presupuesto = int(input("Ingrese el presupuesto: "))
compra = int(input("Ingrese la compra: "))
sobra = presupuesto - compra
print(f'El presupuesto que queda es: {sobra}')

precio_entrada = int(input("Ingrese el precio de la entrada: "))
cantidad_entrada = int(input("Ingrese la cantidad de entradas: "))
print(f'el precio total es de: {precio_entrada*cantidad_entrada}') 

objetos = int(input("Ingrese la cantidad de objetos: "))
personas = int(input("Ingrese la cantidad de personas: "))
obj_pers = objetos/personas
print(f'objetos para cada persona: {obj_pers}')

estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
equipo = int(input("Ingrese la cantidad por equipo: "))
completos = estudiantes // equipo
afuera = estudiantes % equipo
print(f'equipos completos: {completos}')
print(f'estudiantes sin equipo: {afuera}')

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f'{base} elevado a {exponente} es: {base**exponente}')

nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
promedio = (nota1 + nota2 + nota3)/ 3
print(f'el promedio es: {promedio}')