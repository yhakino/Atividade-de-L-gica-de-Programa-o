print("=== Cálculo de Desconto ===")

nome = input("Nome do produto: ")
quantidade = int(input("Quantidade adquirida: "))
preco = float(input("Preço unitário: R$ "))

total = quantidade * preco

if quantidade <= 5:
    desconto = total * 0.02
elif quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05

total_pagar = total - desconto

print("\n----- RESULTADO -----")
print("Produto:", nome)
print("Total: R$ {:.2f}".format(total))
print("Desconto: R$ {:.2f}".format(desconto))
print("Total a pagar: R$ {:.2f}".format(total_pagar))