name = input("Seu nome: ")
hor = input("Qual é o horário? ")

try:
    hora = int(hor)
    if 0 >= hora <= 11:
     print(f"Bom dia,{name}!")
    elif 12 >= hora <= 17:
     print(f"Boa tarde, {name}!")
    elif 18 <= hora <= 24:
     print(f"Boa noite, {name}!")
    else:
     print("Hora inexistente!")
   
except:
   print(f"Digite apenas números inteiros!")