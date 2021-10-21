import numpy as np
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
print(np.inner(a,b))
print(np.outer(a,b))