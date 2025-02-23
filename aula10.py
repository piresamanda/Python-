print("----CALCULADORA----")

while True:
 num1 = input("\nNúmero 1: ")
 num2 = input("Número 2: ")
 operador = input("+ - * /   ")

 numeros_validos = None

 try:
   num1_float=float(num1)
   num2_float=float(num2)
   numeros_validos = True 

   if operador == "+":
     soma = num1_float + num2_float
     print(f"\nsoma = {soma}")
     
   elif operador == "-":
    sub = num1_float - num2_float
    print(f"\nsub = {sub}")
   
   elif operador == "*":
    mult = num1_float * num2_float 
    print(f"\nmult = {mult}")

   elif operador == "/":
    div = num1_float / num2_float
    print(f"\ndiv = {div}")

 except:
   numeros_validos=None

   if numeros_validos is None:
    print("Algum número é inválido!")
    continue

 operadores_validos = "+ - * /"
 if operador not in operadores_validos:
   print("INVÁLIDO!")
   continue
 if len(operador) > 1:
   print("INVÁLIDO!")
   continue
   
 sair = input("Quer sair? [s]im: ").lower().startswith('s')
 print(sair)
