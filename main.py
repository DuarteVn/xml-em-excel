import xmltodict #biblioteca Python que fornece uma maneira de converter dados XML em um dicionário Python e vice-versa.
import os 
import pandas as pd 


def pegar_infos(nome_arquivo, valores):
    # print(f"Pegou as informações {nome_arquivo}") 
                                    #r bits
    with open(f'nfs/{nome_arquivo}', 'rb') as arquivo_xml: #Abrir um arquivo em Python // porque o 'r' de read? Pois está abrindo o arquivo em formato de leitura.         
        dic_arquivo = xmltodict.parse(arquivo_xml) #Transformar esse xml em dicionario python
        #print(json.dumps(dic_arquivo, indent=4)) #Quando ele encontrar uma informação dentro da outra ele vai printar com 4 espaços.
        #json.dumps vai formatar o dicionario para deixar a leitura mais agradável
        
        if 'NFe' in dic_arquivo:
            infos_nf = dic_arquivo['NFe']['infNFe'] #Existem outros tipos de 'NFe' por exemplo "nfeProc"
        else:   
            infos_nf = dic_arquivo["nfeProc"]['NFe']['infNFe']
        numero_nota = infos_nf['@Id']
        empresa_emissora = infos_nf['emit']['xNome']
        nome_cliente = infos_nf['dest']['xNome']
        endereco = infos_nf['dest']['enderDest']
        if 'vol' in infos_nf["transp"]:
            peso = infos_nf["transp"]['vol']['pesoB']
        else:
            peso = 'Peso não informado pela nota.'
        valores.append([numero_nota, empresa_emissora, nome_cliente, endereco, peso])
        

lista_arquivos = os.listdir('NFS')

colunas = ['numero_nota', 'empresa_emissora', 'nome_cliente', 'endereco', 'peso']
valores =[] #Vai começar vazio mas vai adicionar uma lista com os valores que queremos. 


for arquivo in lista_arquivos: 
    pegar_infos(arquivo, valores)
      
tabela = pd.DataFrame(columns=colunas, data=valores) 
tabela.to_excel("NotasFiscais.xlsx", index=False) #Transformando em Excel 
                                    #Porque False? Pq as tabelas do python tem as colunas com o número da linha (012345) eo excel já tem os numero da linha então você não precisa passar os numeros da linha ;)