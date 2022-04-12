import os

a = float(input("Escreva o Primeiro número: "))
b = float(input("Escreva o Segundo número: "))
c = float(input("Escreva o Terceiro número: "))

r = (a+b)*2
s = (b+c)*a

d =(r+s)/4
os.system('clear')

print("Resultado: ",d)
