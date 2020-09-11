import os
import zipfile
import pandas

#Funciona extraindo dos arquivos zipados intradays somente os tickers que você deseja.
#basta substituir a var acao pela string do ticker desejado.

acao = 'BIDI4'

print(">>>>>>>>> INICIO <<<<<<<<<")
for file in os.listdir():
    if file.endswith('.zip'):
        print(file)
        print(">>>>>>>>>>> " + acao + " <<<<<<<<<<<")
        with zipfile.ZipFile(file, 'r') as z:
            for filename in z.namelist():
                if not os.path.isdir(filename):
                    # Ler / Escrever o arquivo:
                    with z.open(filename) as f:                
                        df = pandas.read_csv(f, sep=';')
                        df.info(verbose=False, memory_usage='deep')
                        df[df['TckrSymb'] == acao].to_csv(acao + '.txt', sep=';', index=False, mode='a')
                        del df
print(">>>>>>>>>>> FIM <<<<<<<<<<<")
