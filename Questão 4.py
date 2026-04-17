#variaveis
salario: float 
total_em_vendas: float 
comissao: float
salario_total: float

salario: float = float(input("qual seu salario fixo mensal? "))
total_em_vendas: float = float(input("qual foi o seu faturamento mensal de vendas? "))

if total_em_vendas >= 1500:
    comissao = total_em_vendas * 0.08
else: 
  comissao = total_em_vendas * 0.03

salario_total = comissao + salario

print(salario_total)