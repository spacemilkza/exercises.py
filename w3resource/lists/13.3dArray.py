"""
task: generate a 3d array of 3*4*6
"""

A, B, C = [3, 4, 6], [], []

"""
for a0 in range(A[0]):
    B.append(a0)
print(B)
for a1 in range(A[1]):
    C.append(B)
print(C)
B.clear()
for a2 in range (A[2]):
    B.append(C)
print(C)
C.clear()
"""

C = [x*A[A.index(x ) + 1] for x in A if A.index(x) != A.index(A[-1])]

print(C)
