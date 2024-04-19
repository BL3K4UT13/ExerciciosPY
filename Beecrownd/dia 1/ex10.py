produto_1 = input()
produto_2 = input()

cod_prod_1, qnt_prod_1, preco_prod_1 =  produto_1.split( ) 
cod_prod_2, qnt_prod_2, preco_prod_2 =  produto_2.split( ) 

cod_prod_1 = int(cod_prod_1)
qnt_prod_1 = int(qnt_prod_1)
preco_prod_1 = float(preco_prod_1)

cod_prod_2 = int(cod_prod_2)
qnt_prod_2 = int(qnt_prod_2)
preco_prod_2 = float(preco_prod_2)

subtotal_prod_1 = qnt_prod_1 * preco_prod_1
subtotal_prod_2 = qnt_prod_2 * preco_prod_2

total = subtotal_prod_1 + subtotal_prod_2

print(f"VALOR A PAGAR: R$ {total:.2f}")