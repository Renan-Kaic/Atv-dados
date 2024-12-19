
vetor = []
print("Digite 20 números inteiros:")
for i in range(20):
    valor = int(input(f"Valor {i + 1}: "))
    vetor.append(valor)

vetor_unico = list(dict.fromkeys(vetor))

print("\nVetor sem elementos repetidos:")
print(vetor_unico)