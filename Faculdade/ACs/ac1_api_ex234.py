import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('sqlite///imoveis.db')

class Imovel:
    def __init__(self, id, logradouro, numero, cep):
        pass

def converte_dict_para_imovel(linha):
    d = dict (linha)
    return Imovel(**d)

def pesquisar (nome_rua):
    with engine.connect() as con:
        lista = []
        sql = f"SELECT * FROM imoveis WHERE logradouro = '{nome_rua}'"
        rs = con.execute(sql)
        for linha in rs.fetchall():
            lista.append(converte_dict_para_imovel(linha))
        return lista