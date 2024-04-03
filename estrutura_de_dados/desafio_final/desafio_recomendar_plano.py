def recomendar_plano(consumo):
  if consumo <= 10:
    return "Plano Essencial Fibra - 50Mbps"
  elif consumo > 10 and consumo <= 20:
    return "Plano Prata Fibra - 100Mbps"
  elif consumo > 20:
    return "Plano Premium Fibra - 300Mbps"

consumo = float(input("Digite o seu consumo médio: "))

print(recomendar_plano(consumo))