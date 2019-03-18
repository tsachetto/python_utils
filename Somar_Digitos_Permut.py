#soma os algarismos (dígitos) internos de um número e os escreve em um txt caso preencham uma condição:
#código autoral by tsachetto ;)

import itertools as its

f = open("C:\\Py\\logpy2.txt", "w")
for i in range(1,10):

    a = its.permutations('123456789',i)

    for t in a:
        xx = 0
        soma = (''.join(str(s) for s in t))
        somax = (''.join(str(s) for s in t) + '\n')

        for n in soma:
            xx += int(n)

        if xx == 7:
            f.write(soma + ' - ' + str(xx) + '\n')

f.close()
