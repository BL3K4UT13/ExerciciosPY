num = float(input())

def conta_notas(valor_total, valor_nota): 
    if type(valor_nota) == str:
        print(valor_nota)
    else:
        qnt_notas = 0
        while valor_total >= valor_nota:
            valor_total = valor_total - valor_nota
            qnt_notas += 1
            
        if valor_nota >= 2:
            print(f'{qnt_notas} nota(s) de R$ {valor_nota:.2f}')
        else:print(f'{qnt_notas} moeda(s) de R$ {valor_nota:.2f}')
    return valor_total

ls_valores = ["NOTAS:",100,50,20,10,5,2,"MOEDAS:",1,0.5,0.25,0.10,0.05,0.01]

for valor in ls_valores:
    num = conta_notas(num,valor)
