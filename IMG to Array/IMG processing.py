import numpy as np
import matplotlib.pyplot as plt


width=5
height=4
depth=3


array=np.zeros([height,width,depth],dtype=np.uint8)
print(array)





plt.imshow(array[1])
plt.savefig('Data1.png')
plt.show()
