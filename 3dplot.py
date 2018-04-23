#plot a function of two variables
#using 3D plotting

#3D plotting
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm as CM
from matplotlib.ticker import LinearLocator,FormatStrFormatter
import matplotlib.pyplot as plt

#2d Heat map
from numpy import exp, arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show

#the function that we will plot
def z_func(x,y):
    return (1-(x**2+y**3))*exp(-(x**2+y**2)/2)
    #return 2/(y-(x**2))
#2D
x = arange(-3.0,3.0,0.1) #-3 to 2.9 with spaces of 0.1
y = arange(-3.0,3.0,0.1)

X,Y = meshgrid(x,y) #grid of point
#print(X,Y)
Z = z_func(X,Y)

im = imshow(Z,cmap=cm.RdBu) #drwing the function
#adding the contour lines with labels
cset = contour(Z,arange(-1,1.5,0.2),linewidths=2,cmap=cm.Set2)
clabel(cset,inline=True,fmt='%1.1f',fontsize=10)
colorbar(im)  #adding the colorbar on the right
#latex fashion title
title('$z=(1-x^2+y^3)e^{-(x^2+y^2)/2}$')
show()

#3D
fig = plt.figure('$z=(1-x^2+y^3)e^{-(x^2+y^2)/2}$')
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=CM.RdBu,linewidth=0,antialiased=False)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf,shrink=0.5,aspect=5)
plt.show()