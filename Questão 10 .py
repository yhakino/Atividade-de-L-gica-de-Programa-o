user_code = int(input("Digite seu código de usuário: "))
if user_code != 1234:
    print("Usuário inválido!")
else:
    user_password = int(input("Digite sua senha: "))

    if user_password != 9999:
        print("senha incorreta")
    else:
        print ("Acesso permitido")        