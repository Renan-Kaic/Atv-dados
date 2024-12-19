vetor = []
print("Digite 10 valores para o vetor:")
for i in range(10):
    valor = int(input(f"Valor {i + 1}: "))
    vetor.append(valor)

quantidade_pares = sum(1 for valor in vetor if valor % 2 == 0)

print(f"\nO vetor possui {quantidade_pares} valores pares.")
