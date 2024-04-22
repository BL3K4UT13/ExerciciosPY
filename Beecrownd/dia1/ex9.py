func_nome = str(input())
salario = float(input())
vendas = float(input())

salario_bonus = salario + (vendas * 0.15)

print(f'TOTAL = R$ {salario_bonus:.2f}')