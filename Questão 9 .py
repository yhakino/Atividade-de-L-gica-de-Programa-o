kg_morango = float(input("Quantos kg de morango?: "))
kg_maca = float(input("Quantos kg de maçã?: "))
preco_morango = 0
preco_maca = 0
if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20

if kg_maca <= 5:
    preco_maca = kg_maca * 1.80    
else:
    preco_maca = kg_maca * 1.50

peso_total = kg_maca + kg_morango
valor_total = preco_maca + preco_morango
if peso_total > 8 or valor_total > 25:
    valor_total = valor_total - (valor_total * 0.10)
print(f"O valor total a ser pago é: R${valor_total:.2f}")
