vetor = []
print("Digite 10 valores para o vetor:")
for i in range(10):
    valor = int(input(f"Valor {i + 1}: "))
    vetor.append(valor)

maior = max(vetor)
menor = min(vetor)

print(f"\nO maior elemento é: {maior}")
print(f"O menor elemento é: {menor}")