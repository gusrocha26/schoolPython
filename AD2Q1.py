#SubProgramas
def read_arquivo (entrada,saida):      #Leitura do Arquivo                                     
    line = entrada.readline()                   
    while line!= "" :
        saida.append(line.split())   
        line = entrada.readline()                              

def read_palavras (dados):         #Função para determinar o tamanho das palavras 
    totalpalavras = 0             
    interador = 0                  
    palavra = ""
    for j in range(len(dados)):
        for i in dados[j]:
            if len(i)> totalpalavras:
                palavra = i
                totalpalavras = len(i)
                interador = j + 1
    print("Palavra mais comprida contida no arquivo:", palavra)
    print("Comprimento:", totalpalavras, " caracter(es)")
    print("Localizada na linha ", interador, " do arquivo")


#Programa Principal

Nome_Arquivo = input()
dados_text = []
leitura_dados = open( Nome_Arquivo , "r", encoding='utf-8')
read_arquivo(leitura_dados, dados_text)
leitura_dados.close()

read_palavras(dados_text)
