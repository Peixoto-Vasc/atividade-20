# Crie um programa que utilize uma estrutura de 
# repetição para somar todos os números pares de 1 a 100 e exiba o resultado.
c = 0
for soma in range (1,101):
    if soma % 2 == 0:
        c = c + soma

print(soma)
