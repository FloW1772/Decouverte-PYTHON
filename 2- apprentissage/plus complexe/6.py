def f(**kwargs):
    for key, value in kwargs.items():
        print(key, ':', value)

d = {'cle1': 1, 'cle2': 2, 'cle3': 3}

d2 = {'cle5':5, 'cle6':6, 'cle7':7}


d['cle4'] = 4

d.update(d2)
print(help(d2.get))
#print(d.get('cle8', ))

print(d2.get('nimp', 'par défaut'))

print(help(d.values()))

for k in d.keys():
    print(k)