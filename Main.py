from usuario import Usuario

continuar = 1
lista_usuarios = []

while continuar !=0:
    try:

        nome = input("digite o nome: ")
        idade = int(input("digite sua idade: "))
        sobrenome = input("digite seu sobrenome: ")

        usuario = Usuario(nome,idade,sobrenome)

        lista_usuarios.append(usuario)

        if usuario.idade == 99:
            break

        if usuario.idade == 98:
            continue

        print(f"ola, {usuario.nome} {usuario.sobrenome}, sua idade e {usuario.idade}")

        media_idades = (usuario.idade + usuario.idade) /2
        print(f"A media das idades e: {media_idades}")

        if idade <=17:
            print(f"{usuario.nome} e adolescente")
        elif idade>= 18 and idade<=50:
            print(f"{usuario.nome} e adulto")
        else:
            print(f"{usuario.nome} e idoso")

        continuar = int(input("Deseja continuar cadastrando? 0 -  Sair 1 - Continuar: "))

    except ValueError:
        print("vc dbe informar um numero valido")
else:
    print("Lista de usuarios cadastrados")

    for x in lista_usuarios:
        print(f"Nome completo: {x.nome}, {x.sobrenome} - Idade {x.idade}")

    print("O loop entrou no else")