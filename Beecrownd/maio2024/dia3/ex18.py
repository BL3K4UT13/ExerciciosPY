num = int(input())

def conta_notas(valor_total, valor_nota):
    qnt_notas = 0
    while valor_total >= valor_nota:
        valor_total = valor_total - valor_nota
        qnt_notas += 1
    print(f'{qnt_notas} nota(s) de R$ {valor_nota:.2f}')
    return valor_total

print(num)

ls_valores = [100,50,20,10,5,2,1]

for valor in ls_valores:
    num = conta_notas(num,valor)

