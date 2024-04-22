num = int(input())


notas_100 = 0
while num >= 100:
    num = num - 100
    notas_100 += 1
notas_50 = 0
while num >= 50:
    num = num - 50
    notas_50 += 1
notas_20 = 0
while num >= 20:
    num = num - 20
    notas_20 += 1
notas_10 = 0
while num >= 10:
    num = num - 10
    notas_10 += 1
notas_5 = 0
while num >= 5:
    num = num - 5
    notas_5 += 1
notas_2 = 0
while num >= 2:
    num = num - 2
    notas_2 += 1
notas_1 = 0
while num >= 1:
    num = num - 1
    notas_1 += 1

print(notas_100,"nota(s) de R$ 100,00")
print(notas_50,"nota(s) de R$ 50,00")
print(notas_20,"nota(s) de R$ 20,00")
print(notas_10,"nota(s) de R$ 10,00")
print(notas_5,"nota(s) de R$ 5,00")
print(notas_2,"nota(s) de R$ 2,00")
print(notas_1,"nota(s) de R$ 1,00")
