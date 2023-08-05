# crie uma senha que verifica se uma senha é forte ou fraca,sendo: até 5 = fraca , letras e numeros = forte ,letras numeros e pontuação = Muito forte

def verifica_senha(senha):
    conta_caract = len(senha)
    conta_num = 0
    conta_letras = 0
    conta_pontuacoes = 0
    numeros = ['0', '1', '3', '4','5','6','7','8','9']    
    pontuacoes = [',','.','!',':','?',':']
    for caract in senha:
#        if caract == '0' or caract == '1'or == '3'        
        if caract in numeros:
            conta_num += 1
        if caract.isalpha():
            conta_letras += 1
        if caract in pontuacoes:
            conta_pontuacoes += 1

#  return  conta_caract, conta_num, conta_letras, conta_pontuaçoes
        if conta_caract <= 5:
            return"senha fraca"
        elif conta_letras > 0 and conta_num > 0 and conta_pontuacoes == 0:
            return "senha forte"
        elif conta_letras > 0 and conta_num > 0 and conta_pontuacoes > 0:
            return "Senha Muito Forte"

resultado = verifica_senha('tes,te:123')

print(resultado)
