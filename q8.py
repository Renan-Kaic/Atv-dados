vetor = []
print("Digite 6 valores para o vetor:")
for i in range(6):
    valor = int(input(f"Valor {i + 1}: "))
    vetor.append(valor)

print("\nVetor na ordem inversa:")
for valor in reversed(vetor):
    print(valor)