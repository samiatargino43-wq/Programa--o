import conexao
import json

# Conectar-se ao equipamento R1 do inventário 
# Lendo o arquivo JSON 

with open('inventario.json', "r", enconding="utf-8") as arquivo:
    dados = json.load(arquivo)

# "dados" agora é um dicionário ou lista Python 
print(dados[0]["host"])

cliente=conexao.conectar(dados[0])

# Executar whoami, hostname e uptime -p.

comandos=['whoami', "hostname", "uptime -p"]

for comando in comandos:
codigo,saida,erro=conexao.executar(cliente,comando)
print(f"Código: {codigo}")
print(f"Saída: {saida}")
print(f"Erro: {erro}")
print('========================')


# Exibir,para comando, o código de saída,a saída padrão e a saída de erro.


