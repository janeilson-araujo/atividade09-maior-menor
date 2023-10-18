#Exercício Python 09: faça um software que verifique entre 2 numeros qual o maior

print("saiba qual numero é o maior")
numero1 = int(input("digite o segundo numero:"))
numero2 = int(input("digite o segundo numero:"))

if numero1 < numero2:
   print(f"o numero:{numero2} é o maior e o numero:{numero1} é o menor")
else :
   print(f" o numero:{numero1} é o numero:{numero2} é o menor")