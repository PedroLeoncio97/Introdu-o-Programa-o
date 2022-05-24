#1 - Cadastrar um funcionário e 2 - Listar (imprimir) todos os funcionários
controle = 1
cadastros = []

while controle != 0:
        
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Alterar Funcionario")
    print("4 - Aumentar Salario")
    print("5 - Deletar Funcionario")
    print("0 - Sair")
    
    controle = int(input("Digite a opção: "))

    # Cadastro
    if controle == 1:

        pessoa = []

        nome = input("Digite o nome da pessoa: ")
        pessoa.append(nome)
            
        email = input("Digite o e-mail: ")
        pessoa.append(email)
            
        dataadm = str(input("Digite a dataadm: "))
        pessoa.append(dataadm)
            
        salario = float(input("Digite o salario: R$"))
        pessoa.append(salario)

        cadastros.append(pessoa)
            
            
    # Listar pessoas cadastradas
    elif controle == 2:
            
        if cadastros is None:
                
            print("Não temos registros")
            
        else:
                
            for p in cadastros:
                    
                print(p)

    elif controle == 4:
        if salario <= 1250.00:
            novo_salario = ( salario + (salario * 15 / 100))
        else:
            novo_salario = ( salario + (salario * 10 / 100))

            print("Seu salário agora, com o aumento, é de {:.2f}".format(novo_salario))


    #Ainda vai ser colocado/trabalhado.
    elif controle == 5:
        cadastros.remove()
               

    elif controle == 0:
            
        print("Obrigado! Gostei de interagir com você :\)")
