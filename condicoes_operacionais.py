import random

print("====================================")
print("MISSÃO ACQUA VITA")
print("Equipe Sideralis")
print("====================================")

# Dados simulados

temperatura = random.randint(15, 40)
mare = random.randint(1, 8)

oleo = random.choice(["Sim", "Não"])

plastico = random.choice([
    "Baixo",
    "Médio",
    "Alto"
])

emissao = random.choice(["Sim", "Não"])

# Dados energéticos

energia_solar = random.randint(0, 100)
energia_eolica = random.randint(0, 100)
consumo_energia = random.randint(50, 120)

print("\nCONDIÇÕES OPERACIONAIS\n")

print("Temperatura da água:", temperatura, "°C")
print("Altura da maré:", mare, "m")
print("Mancha de óleo:", oleo)
print("Acúmulo de plástico:", plastico)
print("Emissões ilegais:", emissao)

print("\nSISTEMA ENERGÉTICO\n")

print("Produção Solar:", energia_solar, "%")
print("Produção Eólica:", energia_eolica, "%")
print("Consumo Energético:", consumo_energia, "%")

print("\nALERTAS\n")

alertas = 0

# Temperatura

if temperatura > 30:
    print("ALERTA: Temperatura da água elevada.")
    alertas += 1

# Energia

if energia_solar < 30:
    print("ALERTA: Baixa geração de energia solar.")
    alertas += 1

if energia_eolica < 20:
    print("ALERTA: Baixa geração de energia eólica.")
    alertas += 1

if consumo_energia > 100:
    print("ALERTA: Consumo energético elevado.")
    alertas += 1

# Maré

if mare > 6:
    print("ALERTA: Maré muito alta.")
    print("Risco de enchente costeira.")
    alertas += 1

# Óleo

if oleo == "Sim":
    print("ALERTA: Mancha de óleo detectada.")
    alertas += 1

# Plástico

if plastico == "Alto":
    print("ALERTA: Grande acúmulo de plástico encontrado.")
    alertas += 1

# Emissões

if emissao == "Sim":
    print("ALERTA: Possível emissão ilegal identificada.")
    alertas += 1

if alertas == 0:
    print("Nenhum alerta identificado.")

print("\nCENTRO DE MONITORAMENTO\n")

if oleo == "Sim":
    print("Recomendação: Acionar equipe de contenção do petróleo.")

elif mare > 6:
    print("Recomendação: Avisar regiões costeiras.")

elif consumo_energia > 100:
    print("Recomendação: Reduzir consumo dos sistemas não essenciais.")

elif energia_solar < 30:
    print("Recomendação: Priorizar fontes alternativas de energia.")

elif plastico == "Alto":
    print("Recomendação: Realizar limpeza da área.")

elif temperatura > 30:
    print("Recomendação: Monitorar espécies marinhas.")

else:
    print("Recomendação: Situação estável.")

# Lua

fase_lua = random.choice([
    "Lua Nova",
    "Lua Crescente",
    "Lua Cheia",
    "Lua Minguante"
])

print("\nINFORMAÇÕES COMPLEMENTARES\n")

print("Fase da Lua:", fase_lua)

if fase_lua == "Lua Cheia" and mare > 6:
    print("A Lua Cheia pode estar influenciando a elevação da maré.")

# Relatório da missão

print("\nRELATÓRIO DA MISSÃO\n")

print("Total de alertas:", alertas)

if alertas == 0:
    risco = "Baixo"
elif alertas <= 3:
    risco = "Moderado"
else:
    risco = "Alto"

print("Nível de risco:", risco)

# Desempenho energético

energia_total = energia_solar + energia_eolica
eficiencia = energia_total - consumo_energia

print("\nDESEMPENHO ENERGÉTICO\n")

print("Produção total de energia:", energia_total)

if eficiencia >= 0:
    print("Situação energética: Estável")
else:
    print("Situação energética: Consumo acima da geração")

# Sustentabilidade

indice = 100

if oleo == "Sim":
    indice -= 25

if plastico == "Alto":
    indice -= 20

if emissao == "Sim":
    indice -= 25

if temperatura > 30:
    indice -= 10

print("\nÍNDICE DE SUSTENTABILIDADE\n")

print("Pontuação:", indice, "/100")

if indice >= 80:
    print("Classificação: Excelente")
elif indice >= 60:
    print("Classificação: Boa")
elif indice >= 40:
    print("Classificação: Regular")
else:
    print("Classificação: Crítica")

# Resumo

print("\nRESUMO OPERACIONAL\n")

print("Missão: Acqua Vita")
print("Equipe: Sideralis")
print("Status final:", risco)

if risco == "Alto":
    print("Atenção imediata recomendada.")
elif risco == "Moderado":
    print("Monitoramento reforçado recomendado.")
else:
    print("Operação dentro dos parâmetros esperados.")

print("\nMonitoramento finalizado.")
