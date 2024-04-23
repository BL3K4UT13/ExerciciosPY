def maior_num(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

entrada = input()

a,b,c = entrada.split( )

a = int(a)
b = int(b)
c = int(c)

lista_num = [a,b,c]

resultado = maior_num(lista_num)

print(resultado, 'eh o maior')