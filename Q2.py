# SubProgramas
def ler_dados(entra, saida):
    linha = entra.readline()
    while linha != "":
        saida.append(linha.rstrip('\n').split('#'))
        linha = entra.readline()


def ler_produtos(x, text):
    interador = 0
    w = 0
    for i in range(len(text)):
        if text[i][0] == x:
            w = i
            interador = 1
    if interador == 1:
        print("Produto Localizado:", text[w][0])
        print("Preço Unitario: R$", text[w][2])
        print("Quantidade Disponivel:", text[w][1])
    else:
        print("Produto nao existente")


# Programa Principal
x = input("Nome do produto:")
nomeArquivo = input("Nome do Arquivo:")
text = []
dados = open(nomeArquivo, 'r', encoding='utf-8')
ler_dados(dados, text)
dados.close()
ler_produtos(x, text)
