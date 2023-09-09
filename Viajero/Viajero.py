total_minutos = 0

while True:
    minutos = int(input("Ingrese la duración en minutos del tramo (0 para finalizar): "))

    if minutos == 0:
        break

    total_minutos += minutos

horas = total_minutos // 60
minutos_restantes = total_minutos % 60
print("Tiempo total de viaje:", horas, "horas", minutos_restantes, "minutos")