positivos = ""
negativos = ""

print("Ingrese un valor (Para finalizar ingrese 0): ")

while True:
    num = int(input())

    if num == 0:
        break
    elif num > 0:
        positivos += "*"
    elif num < 0:
        negativos += "*"

print("\nConteo\n")
print("Positivos:", positivos)
print("Negativos:", negativos)