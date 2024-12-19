vetor = []
print("Digite 8 valores para o vetor:")
for i in range(8):
    valor = int(input(f"Valor {i + 1}: "))
    vetor.append(valor)

X = int(input("\nDigite o índice X (entre 0 e 7): "))
Y = int(input("Digite o índice Y (entre 0 e 7): "))

if 0 <= X < 8 and 0 <= Y < 8:
    soma = vetor[X] + vetor[Y]
    print(f"\nA soma dos valores nas posições {X} e {Y} é: {soma}")
else:
    print("\nOs valores de X e Y devem estar entre 0 e 7.")