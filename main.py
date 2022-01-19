import re
import os


def multiplas_trocas(dict, text):
    regex = re.compile(r"(%s)" % "|".join(map(re.escape, dict.keys())), re.IGNORECASE)
    return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], texto)


pasta = './'

caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
txts = [arq for arq in arquivos if arq.lower().endswith(".txt")]


dict = {
'á': 'A',
'Â': 'A',
'â': 'A',
'Á': 'A',
'ã': 'A',
'Ã': 'A',
'É': 'E',
'é': 'É',
'ç': 'C',
'Ç': 'C',
'õ': 'O',
'Õ': 'O',
'ó': 'O',
'Ó': 'O',
'Ô': 'O',
'ô': 'O',
'?': '',
';': '',
'<': '',
'>': '',
'\\': '',
'//': '',
'/': '',
'-': '',
'_': '',
'!': '',
'#': '',
'$': '',
'%': '',
'¨': '',
'&': '',
'*': '',
'(': '',
')': '',
'+': '',
'=': '',
'{': '',
'}': '',
'^': '',
'~': '',
'[': '',
']': '',
'?': '',
':': '',
'¹': '',
'²': '',
'³': '',
'£': '',
'¢': '',
'¬': '',
'ª': '',
'º': '',
'°': '',


}

n = 0 
for txt in txts:
    retirar = './'
    txt = re.sub('./', '', txt)
    print(txt)

    original = open(txt, 'r', encoding='latin-1')
    rel_exp = re.compile(r'[\sa-zA-Z0-9-.]+')
    lista = rel_exp.finditer(str(original.readline()))
    particionado = []

    for itens in lista:
        particionado.append(itens)

    n = n + 1
    os.makedirs('./novos')
    novoTexto = open('./novos/'+particionado[6].group()+'_'+particionado[4].group()+'_00'+str(n)+'.txt', 'w+', encoding='utf-8')
    original.seek(0)
    texto = original.read()
    resultado = multiplas_trocas(dict, texto)
    textopronto, lixo, tail = resultado.partition('SBRCAAEPDR0')
    novoTexto.write(textopronto)
    
    novoTexto.close()
    original.close()
