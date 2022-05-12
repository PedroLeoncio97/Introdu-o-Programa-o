#Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para evitar confusão, chame este dicionário de glossário.
#a - Pense em cinco palavras relacionada à programação que você conheceu nesta disciplina. Use estas palavras como chaves em seu glossário e armazene seus significados como valores.
'''
if - se
else - se nao
print - mostra na tela um resultado ou informação
range - intervalo entre dois pontos
for looping - sistema de repetição 
'''
glossário = {
    'if' : {'nome':'if', 'significado' : 'Condicional'},
    'else' : {'nome':'else', 'significado' : 'Condicional de negação'},
    'print' : {'nome':'print', 'significado' : 'Mostra na tela um resultado ou informação'},
    'range' : {'nome':'range', 'significado' : 'Intervalo entre dois pontos'},
    'for looping' : {'nome': 'for looping', 'significado' : 'sistema de repetição'}
}

print(glossário)

#Mostre cada palavra e seu significado em uma saída, formate a saída de uma forma bem elegante. Por exemplo: você pode exibir a palavra seguida de dois-pontos e depois o seu significado,
#  ou apresentar a palavra em uma linha e então exibir seu significado identado em uma segunda linha. Utilize o caractere de quebra de linha 
# (\n) para inserir uma linha em branco entre cada par palavra-significado em sua saída.

for i in glossário:
    nome = glossário[i]['nome']
    significado = glossário[i]['significado']
    print(f'Durante esse período de aula, aprendemos alguns codigos e metodos da programação em Python, como por exemplo: {nome} quem tem como definição: {significado}.')