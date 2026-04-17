print("Quantos litros vendidos?")
litros = float(input())
print("Qual combustível? (A-> Alcool, G-> Gasolina): ")
combustivel = input().upper()

if combustivel not in ['A', 'G']:
    print("Insira um combustível válido!")
else: 
    if combustivel == 'A':
        preco = 2.90
        if litros <= 20:
            desconto = 0.03  
        else:
            desconto = 0.05
    else:
        preco = 3.30
        if litros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06 

    valorBase = litros * preco
    valorDesconto = valorBase * desconto
    valorAPagar = valorBase - valorDesconto

    print("Valor a ser pago nessas condições: R$ {:.2f}".format(valorAPagar))

    input("\nPressione Enter para sair...")
