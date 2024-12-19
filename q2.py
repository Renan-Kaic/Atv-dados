valores_inteiros = []
print("Digite 6 valores inteiros:")
for i in range(6):
    valor = int(input(f"Valor {i + 1}: "))
    valores_inteiros.append(valor)

print("\nValores lidos:")
for valor in valores_inteiros:
    print(valor)

numeros_reais = []
quadrados = []

print("\nDigite 10 números reais:")
for i in range(10):
    numero = float(input(f"Número {i + 1}: "))
    numeros_reais.append(numero)
    quadrados.append(numero**2)

print("\nVetor original (números reais):")
print(numeros_reais)

print("\nVetor com os quadrados:")
print(quadrados)
