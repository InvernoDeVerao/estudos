opcao = 0
proximo_id = 1
usuarios = []
class User:
    def __init__ (self, id, nome, idade, email):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.email = email

print ('Oque você quer fazer?')
print ('1 para adicionar usuario:')
print ('2 para mostrar os usuarios:')
print ('3 para excluir usuarios -ID-')
print ('4 para fechar')
opcao = input ()

while True:
    if opcao == "1":
        nome = input("escreva seu nome:")
        if any (user.nome == nome for user in usuarios):
            print('Esse nome já existe, tente outra vez:')           
        else:
            idade = int(input("Digite sua idade:"))
            email = input("escreva seu email:")
            if any (user.email == email for user in usuarios):
                print('Esse email já existe, tente outra vez:')
            
            else:
                novo_user = User (proximo_id, nome, idade, email)
                proximo_id += 1
                usuarios.append(novo_user)
                print ("criado")
            
        print ('Oque você quer fazer?')
        print ('1 para adicionar usuario:')
        print ('2 para mostrar os usuarios:')
        print ('3 para excluir usuarios -ID-')
        print ('4 para fechar')
        opcao = input ()

    elif opcao == "2":
        if len(usuarios) == 0:
            print ("Não tem usuarios")
        else:
            for user in usuarios:
                print(f"ID: {user.id} | Nome: {user.nome} | Idade: {user.idade} | email: {user.email}")

        print("Oque você quer fazer?")
        print ('1 para adicionar usuario:')
        print ('2 para mostrar os usuarios:')
        print ('3 para excluir usuarios -ID-')
        print ('4 para fechar')
        opcao = input()

    elif opcao == "3":
        
        if len(usuarios) == 0:
            print("não tem usuarios")
        else:
            id_usuario = int(input("digite o ID que quer deletar:"))

            for user in usuarios:
                if user.id == id_usuario:
                    usuarios.remove(user)
                    print("apagou")
                    break
            else:
                print("Esse ID não existe")

        print("Oque você quer fazer?")
        print ('1 para adicionar usuario:')
        print ('2 para mostrar os usuarios:')
        print ('3 para excluir usuarios -ID-')
        print ('4 para fechar')
        opcao = input()

    elif opcao == '4':
        print ("fechei")
        break
    else:
        print ("opção não existe")
        print ('Oque você quer fazer?')
        print ('1 para adicionar usuario:')
        print ('2 para mostrar os usuarios:')
        print ('3 para excluir usuarios -ID-')
        print ('4 para fechar')
        opcao = input ()
        
