notas = []
print("Digite as notas de 15 alunos:")
for i in range(15):
    nota = float(input(f"Nota do aluno {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"\nA média geral das notas é: {media:.2f}")