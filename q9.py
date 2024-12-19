vetor = []
print("Digite 6 valores pares para o vetor:")
while len(vetor) < 6:
    valor = int(input(f"Valor {len(vetor) + 1}: "))
    if valor % 2 == 0:
        vetor.append(valor)
    else:
        print("Por favor, insira apenas números pares.")

print("\nValores lidos:")
for valor in vetor:
    print(valor)