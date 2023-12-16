import numpy as np
# myarr=np.array([[1,2,3,4,5]])
# myarr

# myarr=np.array([[1,3,4,23,435]])
# myarr

# myarr=np.array([1,3,4,23,435],np.int32)
# print(myarr[3])


# myarr=np.array([[1,9,8,7,5]])
# print(myarr[0,4])

# myarr=np.array([[1,9,8,7,5],[1,9,32,7,5],[1,8,7,5]])
# print(myarr[2,3])
# myarr.shape
# myarr.dtype

# arrlist=np.arry([[1,3,4,2,2],[23,3455,43,24,34,4]])
# print(arrlist)

emp=np.empty((4,6))
print(emp)

space=np.linspace(0,50,10)
print(space)

zero=np.zeros([3,3],dtype=int)
print(zero)

matrix=np.matrix('4,1,12;2,4,3;5,3,7')
print("transpose of matrix")
print(matrix.transpose())

ide=np.identity(5,dtype=int)
print(ide)

print(ide.shape)