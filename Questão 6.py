#var
nome: str
altura: float
sexo: str
peso_ideal: float

nome = input("escreva seu nome ")
altura = float(input("escreva sua altura em numeros e pontos "))

sexo = input("escreva qual seu sexo usando M para masculino e F para feminino ").upper()

if sexo == "M":
    peso_ideal = (72.7*altura) - 58
else:
    peso_ideal = (62.1*altura) - 44.7

print(f"{nome} seu peso ideal é {peso_ideal:.2f}kg")