vetor = []
print("Digite 5 valores:")
for i in range(5):
    valor = float(input(f"Valor {i + 1}: "))
    vetor.append(valor)

maior = max(vetor)
menor = min(vetor)
media = sum(vetor) / len(vetor)

print("\nValores lidos:", vetor)
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Média: {media:.2f}")