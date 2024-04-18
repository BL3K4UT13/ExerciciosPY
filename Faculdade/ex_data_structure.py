dic = {
    "alimentos": {
        "pizzas": ["margueritta", "mussarella", 
                   "frango com catupiry", "portuguesa"],
        "bolos": ("floresta negra", 
                   "red velvet", 
                   "de laranja", "dá vó"),
        "calorias": {
            "leite": 129, "fatia pizza": 320,
            "agua": 0, "maça": 95
            }
    },
    "linguagens": [
        {"nome": "javascript", "criacao": 1996, 
        "paradigma": ["eventos","funcional"]},
        {"nome": "python", "criacao": 1991, 
        "paradigma": ["orientada a objetos","estruturada"]},
        {"nome": "haskell", "criacao": 1990, 
        "paradigma": ["funcional"]}
        ]
    }

#Só se aprende fazendo. PAUSE O VIDEO E TENTE RESPONDER!
#Se possível, FAÇA JUNTO NO SEU COMPUTADOR

#1. quantas chaves tem o dicionario dic?
#print("r1","2")

#2. dic['linguagens'] é uma tupla, um dicionário ou uma lista?
#print("r2","lista")

#3. Como eu faço para mostrar todos os bolos?
#print("r3",dic["alimentos"]["bolos"])

#4. Qual o tipo da lista de todos os bolos?
#print("r4","tupla")

#5. O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
#print(dic["linguagens"]["javascript"]["criacao"])

#print("r5", dic["linguagens"][0]["criacao"])

#6 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
#print(dic["linguagens"][2] == "haskell")
#imprime: false 
#nenhum erro.

#print("r6", dic["linguagens"][2] == "haskell")

#7 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
#print(dic["alimentos"]["pizzas"][2] == "mussarella")
#imprime:false
#erro:nenhum erro.

#print("r7", dic["alimentos"]["pizzas"][2] == "mussarella")

#8 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
#print(1996 in dic['linguagens'][0])
#imprime: false
#erro: nenhum

#print("r8", 1996 in dic['linguagens'][0])

#9 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
#print("criacao" in dic['linguagens'][0])
#imprime: True 
#erro: Nenhum

#print("r9", "criacao" in dic['linguagens'][0])

#9 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
#print("ex9b", "pudim" in dic["sobremesas"]["doces"])
#imprime: false
#erro: KeyError

#print("r9b", "pudim" in dic["alimentos"]["bolos"])

#10 Escreva uma função "mais velha" que 
# recebe um dicionário como dic e 
# retorna (isso é diferente de imprimir!) a linguagem de programação mais velha da nossa lista

def mais_velha(dic):
    lista_linguagem = dic["linguagens"]
    for linguagem in lista_linguagem:
        ling_velha = linguagem["criacao"]
        if ling_velha < linguagem["criacao"]:
            ling_velha = linguagem
    for linguagem in lista_linguagem:
        if ling_velha == linguagem["criacao"]:
            return linguagem

#11 Escreva uma função que retorna uma lista (sem repetições) de paradigmas de linguagens de programação

def paradigmas(dic):
    lista_linguagens = dic["linguagens"]
    lista_parad = []
    for linguagem in lista_linguagens:
        for p in linguagem["paradigma"]:
            if p not in lista_parad:
                lista_parad.append(p)  
    return lista_parad

x = paradigmas(dic)
print(x)

