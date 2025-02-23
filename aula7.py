
name = input(f"Escreva seu nome: ")

if len(name) < 4:
 print(f"Seu nome,'{name}', é curto")
elif 4 <= len(name) <= 6:
 print(f"Seu nome,'{name}', é normal.")
elif len(name) > 6:
 print(f"Seu nome, '{name}', é muito grande")
