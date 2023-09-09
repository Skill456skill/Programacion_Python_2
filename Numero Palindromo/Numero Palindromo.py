print("Ingrese un número: ")
numero_original = int(input())
numero = numero_original
numero_invertido = 0

while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero = numero // 10

if numero_original == numero_invertido:
    print(numero_original, "es un número palíndromo.")
else:
    print(numero_original, "no es un número palíndromo.")