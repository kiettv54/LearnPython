import numpy as np

A = np.array([[1, 2, 3], [3, 4, 5]])
print(A)

A = np.array([[1.1, 2, 3], [3, 4, 5]]) # mảng số thực
print(A)
\
A = np.array([[1, 2, 3], [3, 4, 5]], dtype = complex) # mảng số phức
print(A)
lisarray = [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15]
]
for x in range(len(lisarray)):
    print(lisarray[x])