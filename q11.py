vetor = []
print("Digite 10 números reais:")
for i in range(10):
    valor = float(input(f"Valor {i + 1}: "))
    vetor.append(valor)

negativos = sum(1 for x in vetor if x < 0)
soma_positivos = sum(x for x in vetor if x > 0)

print(f"\nQuantidade de números negativos: {negativos}")
print(f"Soma dos números positivos: {soma_positivos}")