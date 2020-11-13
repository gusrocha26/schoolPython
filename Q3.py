# Subprograma
def table_dict(result, table):    #Função para montar a pontuação da tabela e dos resultados
    val1 = int(result[1])
    val2 = int(result[3])
    if val1 > val2:
        pont1 = 3
        pont2 = 0
    elif val2 > val1:
        pont2 = 3
        pont1 = 0
    else:
        pont1 = 1
        pont2 = 1
    time1 = result[0]
    time2 = result[2]

    table[time1] = pont1
    table[time2] = pont2
    return None

def org_mostra(table, line):          #Função para organizar a tabela
    print()
    print(f"Tabela após {line} partida(s):")
    for chave, valor in sorted(table.items()):
        print(f"{chave} {valor} ponto(s)")
    return None

#Programa Principal

Result = list(input().split("#"))
nulo = ['']
tabela = {}
quant_line = 0
if Result == nulo:
    print("Nenhuma string não vazia foi lida")
else:
    while Result != nulo:
        quant_line += 1
        table_dict(Result, tabela)
        org_mostra(tabela, quant_line)
        print()
        Result = list(input().split("#"))

