import numpy as np

#multi dimensional have more than two square brackets
#creating a multi dimensional array
l1=[1,2,3,4]
l2=[10,20,30,40]
l3=[100,200,300,400]

#create an array
arr=np.array([l1,l2,l3])

#print array
arr

#gives dimension of an array
arr.shape

#resize dimensions of an array
arr.reshape(4,3)