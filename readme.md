#Intersection Of two curves in Pure numpy

Inspired from [this](http://uk.mathworks.com/matlabcentral/fileexchange/11837-fast-and-robust-curve-intersections) matlab implementation, wrote this python implementation of how to detect intersection of two curves.


![image](https://github.com/sukhbinder/intersection/blob/master/images/curve_intersection_python.png)


##Example usage

'''python
a, b = 1, 2
phi = np.linspace(3, 10, 100)
x1 = a*phi - b*np.sin(phi)
y1 = a - b*np.cos(phi)

x2=phi
y2=np.sin(phi)+2
x,y=intersection(x1,y1,x2,y2)
plt.plot(x1,y1,c="r")
plt.plot(x2,y2,c="g")
plt.plot(x,y,"*k")
plt.show()
'''
