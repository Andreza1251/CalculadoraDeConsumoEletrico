

nome_aparelho = input('Qual é o aparelho?')

potencia_aparelho = float(input('Qual é  potência do aparelho em watts (W)?'))

tempo_uso = float(input('Qual é o tempo médio de uso diário em horas?'))

consumo_mensal = (potencia_aparelho * tempo_uso * 30) / 100


print(f'Aparelho -> {nome_aparelho}\nConsumo estimado -> {consumo_mensal} kWh/mês')