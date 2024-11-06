import matplotlib.pyplot as plt
overs=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
runs=[7,21,22,23,24,30,6,7,8,9,10,13,15,13,14,12,20,18,24,28]
plt.plot(overs,runs,marker='x',markerfacecolor='blue',markersize=8,linestyle='dashed',linewidth=2,color='red')
plt.xlabel("overs",color="green")
plt.ylabel("runs",color="orange")
plt.title("YASHAS-1KI23CS185-lineformat")
plt.show()