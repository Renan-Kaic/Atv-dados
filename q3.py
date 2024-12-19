numeros_reais = []
quadrados = []

print("Digite 10 números reais:")
for i in range(10):
    numero = float(input(f"Número {i + 1}: "))
    numeros_reais.append(numero)
    quadrados.append(numero ** 2)

print("\nVetor original (números reais):")
print(numeros_reais)

print("\nVetor com os quadrados:")
print(quadrados)