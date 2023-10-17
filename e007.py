# Um programa que recebe duas notas de um aluno e mostra a sua média
n1 = float(input('Digite a nota do aluno '))
n2 = float(input('Digite a nota do outro aluno '))

media = (n1 + n2) / 2

print ('A media do entre {:.1f} e {:.1f} é {:.2F}'.format(n1,n2,media))

