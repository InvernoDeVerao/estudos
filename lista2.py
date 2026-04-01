NP = []
dados = []

while True:
    dados.append(input("digite seu nome:"))
    dados.append(int(input("digite sua idade:")))
    NP = dados[:]
    
    continuar = input("quer continuar? [S/N]").lower().strip()
    if "n" in continuar:
        break

