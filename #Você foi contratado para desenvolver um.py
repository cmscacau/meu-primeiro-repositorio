#Você foi contratado para desenvolver um programa que calcule a média de notas dos alunos de uma turma. Para isso, você deverá criar uma lista com as notas de cada aluno e, em seguida, implementar uma função que calcule a média aritmética das notas. Além disso, você deverá utilizar um loop while para pedir ao usuário que insira as notas dos alunos até que ele decida parar. Por fim, você deverá utilizar um loop for para imprimir a média de cada aluno.

#a) Escreva o código para a função que calcule a média aritmética das notas.
#b) Escreva o código para o loop while que pede ao usuário que insira as notas dos alunos.
#c) Escreva o código para o loop for que imprime a média de cada aluno.
def media_aluno (nota:float, quantidade:int):
    media = nota / quantidade
    return media
sair = 1
soma_notas = 0
lista_notas = []
while sair == 1:
    quantidade_notas = int(input('quantidade de notas'))
    for i in range(0,quantidade_notas):
        notas = input('digite sua nota')
        soma_notas += notas
        
  # comentando meu codigo a função acima verifica se uma senha é forte ou fraca.  
    
    