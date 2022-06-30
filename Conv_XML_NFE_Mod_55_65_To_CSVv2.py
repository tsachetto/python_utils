import os
import pandas as pd
import csv
from os import walk
from bs4 import BeautifulSoup
import re

#CONVERSOR DE XML NFE OU NFCE PARA TEXTO / Convert Brazilian NF-E XML (Model 55 or 65) to CSV
#VERSÃO 7.0b de 08/2021 - Necessary: Python 3.0+
#Como usar / How to use:
#Copie todo este texto para um txt em branco e salve em uma pasta em branco ex: conversor.py / Copy this whole text into a new txt file and save it into a new folder, ex.: conversor.py
#Coloque alguns arquivos XML de NF mod 65 ou 55 na pasta e execute o arquivo conversor.py / Put some NFE XML into the folder and run the conversor.py file.
#Pronto, ele irá gerar um arquivo CSV contendo os dados dos XMLs. / Done! It will born a new CSV file with the XML content on it!
#Obrigado / thanks!
#Thomaz Sachetto Silva +55 32 98409-5689

print("Iniciando processamento de notas fiscais...")

f = []
for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    f.extend(filenames)
    break

rows = ['Emissao', 'NFE', 'Serie', 'Mod', 'CNPJ_Emit', 'NOME_Emit', 'UF_Emit', 'IE_Emit', 'CRT', 'CNPJ_Dest', 'NOME_Dest', 'UF_Dest', 'IE_Dest',
        'CONS_Final', 'Cdg_Produto', 'Descricao_Produto', 'Und_Produto', 'Qtd_Produto', 'Valor_Unit', 'Valor_Produto', 'Desconto', 'Origem', 'EAN',
        'CFOP', 'NCM', 'ICMS_CST', 'ICMS_BC', 'ICMS_Aliq', 'ICMS_Valor', 'CEST', 'ICMSST_Mod', 'ICMSST_MVA', 'ICMSST_BC',
        'ICMSST_Alq', 'ICMSST_Valor','ICMS_Difal', 'ICMS_FCP', 'IPI_CST', 'IPI_BC', 'IPI_Alq', 'IPI_Valor', 'PIS_CST', 'PIS_BC', 'PIS_Alq',
        'PIS_Valor', 'COFINS_CST', 'COFINS_BC', 'COFINS_Alq', 'COFINS_Valor', 'DESP_Acess', 'SEGURO_Total', 'FRETE_Total', 'Chave_Acesso']

dataList = [rows]

for xml in f:
    if("xml" in xml):
        with open(xml, 'r', encoding='utf8') as f:
            print("Processando", xml)
            data = f.read()
            soup = BeautifulSoup(data, 'lxml')

            items = soup.find_all('det')

            for item in items:


                #AQUI COMEÇA O PREENCHIMENTO DAS VARIAVEIS
                
                #valor icms
                try:
                    icmsv = item.find('icms').find(re.compile("vicms")).getText().replace(".",",")
                    icmsalq = item.find('icms').find(re.compile("picms")).getText().replace(".",",")
                    icmsbc = item.find('icms').find(re.compile("vbc")).getText().replace(".",",")
                except:
                    icmsv = 0
                    icmsalq = 0
                    icmsbc = 0

               #origem
                try:
                    origem = item.find('icms').find('orig').getText()
                except:
                    origem = "-"                    

               #origem
                try:
                    cean = item.find('cean').getText()
                except:
                    cean = "-"     

                #ipi cst
                try:
                    ipicst = item.find('ipi').find(re.compile("cst")).getText()
                except:
                    ipicst = 0
                #bc ipi
                try:
                    ipibc = item.find('ipi').find(re.compile("vbc")).getText().replace(".",",")
                except:
                    ipibc = 0

                #bc alq
                try:
                    ipialq = item.find('ipi').find(re.compile("pipi")).getText().replace(".",",")
                except:
                    ipialq = 0
                #valor ipi
                try:
                    ipiv = item.find('ipi').find(re.compile("vipi")).getText().replace(".",",")
                except:
                    ipiv = 0

                #valor desconto prod
                try:
                    vdesc = item.find('prod').find(re.compile("vdesc")).getText().replace(".",",")
                except:
                    vdesc = 0

                #valores pis
                try:
                    pisbc = item.find('pis').find('vbc').getText().replace(".",",")
                    pisalq = item.find('pis').find('ppis').getText().replace(".",",")
                    pisvr = item.find('pis').find('vpis').getText().replace(".",",")

                except:
                    pisbc = 0
                    pisalq = 0
                    pisvr = 0

               #cst do pis
                try:
                    piscst = item.find('pis').find('cst').getText()
                except:
                    piscst = "-"

               #cst do cofins
                try:
                    cofinscst = item.find('cofins').find('cst').getText()
                except:    
                    cofinscst = "-"
                    
                #valores cofins
                try:
                    cofinsbc = item.find('cofins').find('vbc').getText().replace(".",",")
                    cofinsalq = item.find('cofins').find('pcofins').getText().replace(".",",")
                    cofinsvr = item.find('cofins').find('vcofins').getText().replace(".",",")
                except:
                    cofinsbc = 0
                    cofinsalq = 0
                    cofinsvr = 0
                #emitente nome
                try:
                    emitnome = soup.find('emit').find('xnome').getText()
                except:
                    emitnome = "-"
                #CRT - Regime Trib do Emitente
                try:
                    crtemit = soup.find('emit').find('crt').getText()
                except:
                    crtemit = "-"                    
                #destinatario nome
                try:
                    destnome = soup.find('dest').find('xnome').getText()
                except:
                    destnome = "-"
                #produto nome
                try:
                    prodnome = item.find('xprod').getText()
                except:
                    prodnome = "-"

                #produto codigo
                try:
                    codprod = item.find('cprod').getText()
                except:
                    codprod = "-"
                #transporte
                try:
                    vfrete = item.find('vfrete').getText().replace(".",",")
                except:
                    vfrete = 0
                #despesas acessorias
                try:
                    voutros = item.find('voutro').getText().replace(".",",")
                except:
                    voutros = 0                    
                #seguro
                try:
                    vseguro = soup.find('total').find('vseg').getText().replace(".",",")
                except:
                    vseguro = "-"
                 #modst
                try:
                   stmod = item.find('icms').find('modbcst').getText()
                except:
                   stmod = 0
                 #cest
                try:
                    stcest = item.find('cest').getText()
                except:
                    stcest = "-"                   
                 #mva
                try:
                    stmva = item.find('icms').find('pmvast').getText().replace(".",",")
                except:
                   stmva = 0
                 #bc st
                try:
                    stbc = item.find('icms').find('vbcst').getText().replace(".",",")
                except:
                    stbc = 0
                #alqst
                try:
                    stalq = item.find('icms').find('picmsst').getText().replace(".",",")
                except:
                    stalq = 0
                #vr st
                try:
                    stvr = item.find('icms').find('vicmsst').getText().replace(".",",")
                except:
                    stvr = 0

                #ie emitente
                try:
                    ieemit = soup.find('emit').find('ie').getText()
                except:
                    ieemit = "-"
                #ie dest
                try:
                    iedest = soup.find('dest').find('ie').getText()
                except:
                    iedest = "-"
                    

                #uf emitente
                try:
                    ufemit = soup.find('emit').find('uf').getText()
                except:
                    ufemit = "-"

                #uf dest
                try:
                    ufdest = soup.find('dest').find('uf').getText()
                except:
                    ufdest = "-"                    

                #cnpj emitente
                cn = 0    
                try:
                    cnpjemit = str(soup.find('emit').find('cnpj').getText())
                except:
                    cn = 1

                if cn == 1:
                    try:
                        cnpjemit = str(soup.find('emit').find('cpf').getText())                        
                    except:
                        cnpjemit = "-"                

                #cnpp dest
                cj = 0
                try:
                    cnpjdest = str(soup.find('dest').find('cnpj').getText())
                except:
                    cj = 1

                if cj == 1:
                    try:
                        cnpjdest = str(soup.find('dest').find('cpf').getText())                        
                    except:
                        cnpjdest = "-"

                #ICMS Difal / FCP
                try:
                    icmsdifal = item.find('icmsufdest').find('vicmsufdest').getText().replace(".",",")
                except:
                    icmsdifal = 0
                
                try:
                    icmsfcp = item.find('icmsufdest').find('vfcpufdest').getText().replace(".",",")
                except:
                    icmsfcp = 0

                #indicador de consumidor final
                indf = soup.find('ide').find('indfinal').getText()          

                if indf == '0':
                    indfinal = "Nao"
                if indf == '1':
                    indfinal = "Sim"

                #AQUI COMEÇA A LISTA           

                dataList.append([
                    soup.find('ide').find('dhemi').getText()[:10],
                    soup.find('ide').find('nnf').getText(),
                    soup.find('ide').find('serie').getText(),
                    soup.find('ide').find('mod').getText(),                    
                    cnpjemit,
                    emitnome,
                    ufemit,
                    ieemit,
                    crtemit,
                    cnpjdest,
                    destnome,
                    ufdest,
                    iedest,
                    indfinal,
                    codprod,
                    prodnome,
                    item.find('ucom').getText(),
                    item.find('qcom').getText().replace(".",","),
                    item.find('vuncom').getText().replace(".",","),
                    item.find('vprod').getText().replace(".",","),
                    vdesc,
                    origem,
                    cean,
                    item.find('cfop').getText(),
                    item.find('ncm').getText(),
                    item.find('icms').find(re.compile("cs")).getText(),
                    icmsbc,
                    icmsalq,
                    icmsv,
                    stcest,
                    stmod,
                    stmva,                    
                    stbc,
                    stalq,
                    stvr,
                    icmsdifal,
                    icmsfcp,
                    ipicst,
                    ipibc,
                    ipialq,
                    ipiv,
                    piscst,
                    pisbc,
                    pisalq,
                    pisvr,
                    cofinscst,
                    cofinsbc,
                    cofinsalq,
                    cofinsvr,
                    voutros,
                    vseguro,
                    vfrete,                    
                    'ch' + soup.find('chnfe').getText(),
                    ])

                pd.DataFrame(dataList).to_csv("{DATEME}.csv", quoting=csv.QUOTE_NONNUMERIC, index=False, header=False, sep=';')

print("Processamento finalizado com sucesso")
