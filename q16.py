vetor = []
print("Digite 5 números reais para o vetor:")
for i in range(5):
    valor = float(input(f"Valor {i + 1}: "))
    vetor.append(valor)

codigo = int(input("\nDigite o código (0 para sair, 1 para ordem direta, 2 para ordem inversa): "))

if codigo == 0:
    print("Programa finalizado.")
elif codigo == 1:
    print("\nVetor na ordem direta:", vetor)
elif codigo == 2:
    print("\nVetor na ordem inversa:", list(reversed(vetor)))
else:
    print("\nCódigo inválido.")