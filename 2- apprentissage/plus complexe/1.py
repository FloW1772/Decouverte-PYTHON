import operator

def f(**kwargs):
    for key, value in kwargs.items():
        print(key, ':', value)

d = {'cle1': 20, 'cle2': 10}

for k, v in sorted(d.items(), key = operator.itemgetter(0)):
    print(k, v)

print(dir(dict))