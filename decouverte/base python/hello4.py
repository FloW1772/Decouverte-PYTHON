def f(a, b, /, d, e, *, c=10):
    print(a, b, c, d, e)
    # return a + b + c

f('world', 'python', d='param d', e="dgdsg", c='hello')
