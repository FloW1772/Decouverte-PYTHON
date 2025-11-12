def f(a, b, *integers, c):
    print(a, b)
    for i in integers:
        print("elemnt:", i)

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

f(a='a', b='b', *t, c=11)