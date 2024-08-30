import json

# Simulando o conteúdo de um arquivo JSON
dados_json = '''
{
    "faturamento": [
        {"dia": 1, "valor": 22174.1664},
        {"dia": 2, "valor": 24537.6698},
        {"dia": 3, "valor": 26139.6134},
        {"dia": 4, "valor": 0.0},
        {"dia": 5, "valor": 0.0},
        {"dia": 6, "valor": 26742.6612},
        {"dia": 7, "valor": 0.0},
        {"dia": 8, "valor": 42889.2258},
        {"dia": 9, "valor": 46251.174},
        {"dia": 10, "valor": 11191.4722}
    ]
}
'''

# Carregar os dados do JSON
dados = json.loads(dados_json)
faturamento = [dia['valor'] for dia in dados['faturamento'] if dia['valor'] > 0]

# Cálculos
menor_valor = min(faturamento)
maior_valor = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_media = sum(1 for valor in faturamento if valor > media_mensal)

# Resultados
print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
print(f"Número de dias acima da média mensal: {dias_acima_media}")