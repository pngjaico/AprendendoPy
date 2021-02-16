
def media_nota(notas):
    quantidade = len(notas)
    soma = sum(notas)
    media = soma/quantidade
    print (f'O aluno tirou {media}')
    if media >= 7:
        print ('Aluno está com média')
    else: 
        print ('Aluno não está com média')

lista = input('Qual são as notas?: ').split()
lista = [int(item) for item in lista]
media_nota(lista)