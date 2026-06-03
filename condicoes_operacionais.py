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

print("\nANÁLISE DA IA\n")

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

    fase_lua = random.choice([
        "Lua Nova",
        "Lua Crescente",
        "Lua Cheia",
        "Lua Minguante"
    ])

    print("Fase da Lua:", fase_lua)

    if fase_lua == "Lua Cheia" and mare > 6:
        print("A Lua Cheia pode estar influenciando a elevação da maré.")