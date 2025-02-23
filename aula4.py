nome = input("Nome: ")
idade = input("Idade: ")

if nome and idade: 
    print(f"Você se chama {nome}")
    print(f"'{nome[::-1]}' é o seu nome invertido")
    if ' ' in nome:
        print(f"'{nome}' contém espaço")
    else:
        print(f"Seu nome NÃO contém espaços")
    print(f"Seu nome tem {len(nome)} caracteres")
    print(f"A primeira letra do seu nome é '{nome[0]}'")
    print(f"A última letra do seu nome é '{nome[-1]}'")
else:
    print("Tente novamente!")