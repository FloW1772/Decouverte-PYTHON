from copy import deepcopy

L = [['d', 'a', 'd', 'f'], ['c']]

#L2 = L
#L2 = L[:]
#L2 = L.copy()
L2 = deepcopy(L)

L2[1].append('z')

print(L)