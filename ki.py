from numpy import array
from numpy import tensordot
A=array([
[[1,2,3],[4,5,6],[7,8,9]],    
[[11,12,13],[14,15,16],[17,18,19]],
[[21,22,23],[24,25,26],[27,28,29]]
])
print(A.shape)
print("A matrix is/n",A)
B=array([
[[1,2,3],[4,5,6],[7,8,9]],    
[[11,12,13],[14,15,16],[17,18,19]],
[[21,22,23],[24,25,26],[27,28,29]]
])
print(B.shape)
print("B matrix is/n",B)
print("tensor addition is/n")
C=A+B
print(C.shape)
print("the addition result C matrix/n",C)
print("tensor substraction is/n")
S=A-B
print(S.shape)
print("the differences S matrix /n",S)
print("tensor multiplication is/n")
M=A*B
print(M.shape)
print("the product of scalar result matrix/n",M)
print("tensor division is/n")
D1=A/B
print(D1.shape)
print("the division D1 matrix/n",D1)
D=array([1,2])
E=array([3,4])
F=tensordot(D,E,axes=0)
print("result wen axes=0/n",F)
F=tensordot(D,E,axes=1)
print("result wen axes=1/n",F)