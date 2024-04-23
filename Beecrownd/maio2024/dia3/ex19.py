entrada = int(input())

horas = 0
while entrada >= 3600:
    entrada = entrada - 3600
    horas += 1

minutos = 0
while entrada >= 60:
    entrada = entrada - 60
    minutos += 1

segundos = entrada

print(horas,":",minutos,":",segundos)