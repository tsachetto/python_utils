#Read Trade Intraday
list = ['0904']

f0 = open("consultas.txt","r")

#loop no txt de ativos para consulta
for tk in f0:

    ticker = tk[0:6] #input("Insira o Ticker do Ativo desejado: ")
    print(tk)
    #loop em cada Intraday
    for i in list:

        periodo = "2020" + str(i) #input("Insira o período desejado, ex. 20200819: ")

        texto = "TradeIntraday_" + periodo + "_1.txt"
        ativo = ticker + "-" + periodo + ".txt"
        acao = "Ativo\\Novo\\" + ticker + ".txt"


        f1 = open(texto,"r")
        f2 = open(acao,"a+")
        
        #loop pelas linhas do Intraday ativo
        for line in f1:
            if line[11:17] == ticker:
                f2.write(line)        

        #f2.write("\n")
        f1.close()
        f2.close()

f0.close()
#End Read Trade Intraday
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Get Tickers Pandas
import pandas

df = pandas.read_csv('TradeIntraday_20200904_1.txt', sep=';', usecols=[1]).drop_duplicates(keep='first').reset_index()
df.to_csv('Tickers.txt', index=False)
#End Get Tickers Pandas
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



