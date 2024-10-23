import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(1,20,7)
y1=x
y2=np.square(x)
y3=np.sqrt(x)
print(y1)
print(y2)
print(y3)
plt.plot(x,y1,'red',x,y2,'green',x,y3,'blue')
plt.legend(['x','square x','sqrt x'])
plt.xticks(x)
plt.yticks(y2)
plt.xlabel("xaxis",fontsize=12)
plt.ylabel("yaxis",fontsize=12)
plt.title("Linear-yashas-1KI23CS185")
plt.show()