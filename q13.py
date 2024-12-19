vetor = []
print("Digite 5 valores:")
for i in range(5):
    valor = float(input(f"Valor {i + 1}: "))
    vetor.append(valor)

maior = max(vetor)
menor = min(vetor)
pos_maior = vetor.index(maior)
pos_menor = vetor.index(menor)

print(f"\nPosição do maior valor ({maior}): {pos_maior}")
print(f"Posição do menor valor ({menor}): {pos_menor}")