import numpy as np
import matplotlib.pyplot as plt


Data=plt.imread('Ana.png')
print(Data)



face=Data[50:225,300:475]
face1=Data[50:225:4,300:475:4]




#How to save the data
#data=np.ravel(face)
#np.savetxt('Ana_face.txt',data)


plt.imshow(face)
plt.show()
