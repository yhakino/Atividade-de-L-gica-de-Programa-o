ano_atual=(int(input('Em que ano estamos?')))
ano_nasc=(int(input('Em qual ano você nasceu?')))
idade=ano_atual-ano_nasc+

if idade<16:   
    print(f'Infelizmente você não pode votar ainda,pois você tem apenas {idade} anos!')

elif idade>=16:
    
    print(f'Você pode votar esse ano, pois você tem {idade} anos!')