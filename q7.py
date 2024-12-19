vetor = []
print("Digite 10 valores para o vetor:")
for i in range(10):
    valor = int(input(f"Valor {i + 1}: "))
    vetor.append(valor)

maior = max(vetor)
posicao = vetor.index(maior)

print("\nVetor:", vetor)
print(f"O maior elemento é {maior} e está na posição {posicao}")