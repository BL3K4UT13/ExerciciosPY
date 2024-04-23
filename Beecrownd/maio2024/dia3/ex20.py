entrada = int(input())

anos = 0
while entrada >= 365:
    entrada = entrada - 365
    anos += 1

meses = 0
while entrada >= 30:
    entrada = entrada - 30
    meses += 1

dias = entrada

print(anos,"ano(s)")
print(meses,"mes(es)")
print(dias,"dia(s)")