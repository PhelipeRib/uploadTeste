aluno = str(input('digite o nome do aluno: '))
p1 = float(input('digite a nota da primeira prova: '))
p2 = float(input('digite a nota da segunda prova: '))
p3 = float(input('digite a nota da terceira prova: '))
media = (p1 + p2 + p3)/3
print(media)
if media < 5:
    print(aluno, 'foi reprovado por nota')
elif media >= 5 and media < 7:
    print(aluno, 'ficou em exame final')
else:
    print(aluno, 'foi aprovado')