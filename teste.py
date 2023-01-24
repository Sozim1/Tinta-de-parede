print("\nEsta é uma calculadora que ira te mostrar quantos litros de tintas seram nescessario para pintar sua parede :)")
lag = float(input("\nMe diz, qual a largura de sua parede? "))
alt = float(input("Entendi, agora meu parceiro me fala a altura dela: "))
area = (lag * alt)
print("\nPerfeito sendo assim {} x {} ira resultar em {}m2".format(alt, lag, area))

tinta = area / 2

if tinta > 10:
  print("Oloco vai pintar um predio? Por que vai ser nescessario {} litros de tinta para pintar esse mural".format(tinta))
else:
  print("Sendo nescessario {} Litros de tinta".format(tinta))