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

print("\nCONDIÇÕES OPERACIONAIS\n")

print("Temperatura da água:", temperatura, "°C")
print("Altura da maré:", mare, "m")
print("Mancha de óleo:", oleo)
print("Acúmulo de plástico:", plastico)
print("Emissões ilegais:", emissao)

print("\nALERTAS\n")

# Temperatura

if temperatura > 30:
    print("ALERTA: Temperatura da água elevada.")

# Energia

energia_solar = random.randint(0, 100)
energia_eolica = random.randint(0, 100)
consumo_energia = random.randint(50, 120)

print("Produção Solar:", energia_solar, "%")
print("Produção Eólica:", energia_eolica, "%")
print("Consumo Energético:", consumo_energia, "%")

if energia_solar < 30:
    print("ALERTA: Baixa geração de energia solar.")

if energia_eolica < 20:
    print("ALERTA: Baixa geração de energia eólica.")

if consumo_energia > 100:
    print("ALERTA: Consumo energético elevado.")

# Maré

if mare > 6:
    print("ALERTA: Maré muito alta.")
    print("Risco de enchente costeira.")

# Óleo

if oleo == "Sim":
    print("ALERTA: Mancha de óleo detectada.")

# Plástico

if plastico == "Alto":
    print("ALERTA: Grande acúmulo de plástico encontrado.")

# Emissões

if emissao == "Sim":
    print("ALERTA: Possível emissão ilegal identificada.")

print("\nCENTRO DE MONITORAMENTO\n")

if oleo == "Sim":
    print("Recomendação: Acionar equipe de contenção do petróleo.")

elif mare > 6:
    print("Recomendação: Avisar regiões costeiras.")

elif temperatura > 30:
    print("Recomendação: Monitorar espécies marinhas.")

elif plastico == "Alto":
    print("Recomendação: Realizar limpeza da área.")

else:
    print("Recomendação: Situação estável.")

# Lua

fase_lua = random.choice([
    "Lua Nova",
    "Lua Crescente",
    "Lua Cheia",
    "Lua Minguante"
])

print("\nINFORMAÇÕES COMPLEMENTARES")
print("Fase da Lua:", fase_lua)

if fase_lua == "Lua Cheia" and mare > 6: 
    print("A Lua Cheia pode estar influenciando a elevação da maré.") 
print("\nMonitoramento finalizado.")
