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
           