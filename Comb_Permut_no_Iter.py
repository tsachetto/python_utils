#Funções legais do itertools!
permutations("123456", 6)
for i in list(a):
    print(i)


#Em desenvolvimento...

#Agora uma especial:

import itertools as its

a = its.permutations("123456789", 9)

f = open("C:\\Py\\logpy2.txt", "w")
for t in a:
    f.write(' '.join(str(s) for s in t) + '\n')
f.close()

#fim da especial
hoho
