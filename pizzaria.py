

sabores = ["Frango", "Calabresa", "Portuguesa", "Marguerita", "Banana com canela"]
bordas = ["Catupiry - R$10", "Cheddar - R$12", "Chocolate - R$15"]
valores_bordas = [10, 12, 15]
tamanhos = ["Família - R$65", "Médio - R$55", "Pequeno - R$45"]
valores_tamanhos = [65,55, 45]
divisoes = ["Metade", "Inteira"]
valores_divisoes = [15, 0]
regioes = ["Samambaia", "Sudoeste", "Guará", "Asa Sul"]
valores_regioes = [15, 18, 22, 25]

#Título inicial
print("----PIZZARIA----\n")

# Exibir opções de sabores
for i, s in enumerate(sabores, 1):
    print(f"{i}. {s}")

# Capturar escolha do usuário
try:
    escolha_sabor1 = int(input("\nQual sabor da sua pizza?: "))
    for i, s in enumerate(sabores,1):
        sabor_um = sabores[escolha_sabor1 - 1]

    valor_pedido = [] #Lista para armazenar os valores 

    #Borda
    print("\nDeseja adicionar borda?: ")
    resposta_borda = input("[S] ou [N]: ").strip().lower()

    if resposta_borda == "s":
      print("\nEscolha uma borda: ")
      for i, b in enumerate(bordas, 1):
          print(f"{i}. {b}")
      escolha_borda= int(input()) - 1
      borda = bordas[escolha_borda]

      valor_borda = valores_bordas[escolha_borda]  # Pega o valor numérico da borda
      valor_pedido.append(valor_borda) #Adiciona o valor da borda na lista valor_pedido
      
    else: 
      escolha_borda=None

    #Tamanho
    print("\nEscolha o tamanho da pizza: ")
    for i, t in enumerate(tamanhos, 1):
      print(f"{i}. {t}")
    tamanho = int(input()) - 1
    valor_pedido.append(valores_tamanhos[tamanho])

    #Divisão
    print("\nDeseja dividir a pizza?: ")
    resposta_divisao = input("[S] ou [N]: ").strip().lower()

    if resposta_divisao == "s":
      print("\nEscolha o 2° sabor: ")
      for i, s in enumerate(sabores, 1):
        print(f"{i}. {s}")
      escolha_sabor2 = int(input()) - 1 #Captura o 2ºsabor
      sabor_dois = sabores[escolha_sabor2] #Armazena o 2ºsabor
      valor_pedido.append(valores_divisoes[0]) #Adiciona o valor 
    else:
     sabor_dois = None #Caso nã haja divisão
      
    #Região
    print("\nEscolha sua região: ")
    for i, r in enumerate(regioes,1):
     print(f"{i}. {r}")
    regiao = int(input()) -1
    valor_pedido.append(valores_regioes[regiao]) #Adiciona o valor

   #Calcular valor do pedido 
    print("\n----PEDIDO----\n")

    total = sum(valor_pedido) #Calcula o valor de todos os itens

    #Exibe o pedido  
    if resposta_divisao == "s":
     print(f"Sabor:", sabor_um, "com", sabor_dois )  
    else:
      print(f"Sabor:", sabor_um)

    if resposta_borda == "s":
      print(f"Borda:", borda)

    print(f"Tamanho:", tamanhos[tamanho])
    print(f"Região:", regioes[regiao])
    print("\n----VALOR----\n")
    print(f"Total: R${total}")
          
except ValueError:
    print("Por favor, digite um número válido.")
