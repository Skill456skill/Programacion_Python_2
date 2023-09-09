print("Ingrese la cantidad de datos que ingresará: ")
num_datos = int(input())

minimo = float('inf')
maximo = float('-inf')

for i in range(num_datos):
    print("Ingrese el dato", i + 1, ": ", end="")
    dato = float(input())

    if dato < minimo:
        minimo = dato
    if dato > maximo:
        maximo = dato

# Calcular y mostrar el rango de los datos
rango = maximo - minimo
print("El rango de los datos ingresados es:", rango)