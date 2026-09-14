# Etapa 1: Cadastro da Startup e Projetos
Startup = {
    "nome": "CyberPulse Tech",
    "segmento": "Segurança da Informação",
    "ano_adesao": "2026"
}

solucao_ativa = ["Firewall", "IA", "Scan de Vulnerabilidades"]
print("Startup:", Startup["nome"], "Segmento:", Startup["segmento"], "Produto:", solucao_ativa[0])

# Etapa 2: Mapeamento das Bancadas de Trabalho (Matriz 2D)
bancadas = ([1,0],
            [0,1])
print("Bancada N1:", bancadas[0][0], "Bancada N2:", bancadas[0][1], "Bancadas N3:", bancadas[1][0], "Bancada N4:", bancadas[1][1])
print("1 = Ocupado e 0 = Livre")

# Etapa 3: Criação da Base de Dados e Elaboração do Prompt de Leitura

with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    Linha1 = arquivo.readline()
    Linha2 = arquivo.readline()
    Linha3 = arquivo.readline()
    Linha4 = arquivo.readline()

print(cabecalho, end="")
print(Linha1, end="")
print(Linha2, end="")
print(Linha3, end="")
print(Linha4)

#  Etapa 4: Elaboração do Prompt para Painel e Cálculo Final

total = sum(
    float(linha.split(",")[1].strip())
    for linha in (Linha1, Linha2, Linha3, Linha4)
)

print("Nome da startup:", Startup["nome"])
print("Bancada alocada: Bancada N1")
print(f"Total de infraestrutura cloud: {total:.2f}")
