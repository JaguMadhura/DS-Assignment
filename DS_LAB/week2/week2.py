import numpy as np
N1=np.array([1,2,3,4])
N2=np.array([5,6,7,8])
print(type(N1))
#array indexing
print(N1[0])
#negative indexing
print(N1[-2])
#Array slicing
print(N1[2:4])
print(N1[:3])
print(N2[3:])
#Initialize numpy array

N1=np.zeros((3,4))
print(N1)
print(type(N1))
#checking dimeansion
print(N1.ndim)
#shape of an array
p=np.array([[[1,2,3,4],[5,6,7,8]]])

print(p.shape)
#Reshape of the array
print(N1.reshape(2,6))
#looping in 1 array
for i in N1:
    print(i)
#concatenate array
N3=np.concatenate((N1,N2))
print(N3)
#splitting array
print(np.array_split(N3,4))
#accesing individual array after splitting
sp=np.array_split(N3,4)
print(sp[0])
#searching 
p=np.where(N2==3)
print(p)
#sorting 
p=np.sort(N1)
print(p)
#arithmetic operations
#sum
print(np.sum((N1,N2)))
#subtract
print(np.subtract(N1,N2))
#multiply
print(np.multiply(N1,N2))
#division
print(np.divide(N1,N2))