def f(**kwargs):
    for key, value in kwargs.items():
        print(key, ':', value)

d = {'a': 1, 'b': 2, 'c': 3}

f(**d)