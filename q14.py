vetor = []
print("Digite 10 valores para o vetor:")
for i in range(10):
    valor = int(input(f"Valor {i + 1}: "))
    vetor.append(valor)

repetidos = set(x for x in vetor if vetor.count(x) > 1)

if repetidos:
    print("\nValores repetidos:", repetidos)
else:
    print("\nNão há valores repetidos.")