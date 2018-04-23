#Visual6__________________________Uso de pylab

from pylab import plot, ylim, show
from numpy import linspace,sin,cos
import pylab

x = linspace(0,10,100)
y1 = sin(x)
y2 = cos(x)
plot(x,y1,"go")   #colores: r,g,b,c,m,y,k,w:...cyan,magenta,yellow,black and white
          #tambien puede "r--" que es red y rayitas pautadas
plot(x,y2,"r--")
ylim(-1.1,1.1)  #Esto hace mas espacioso el alto de la grafica y permite la visualizacion correcta
pylab.xlabel("Eje x")
pylab.ylabel("Eje y: sen(x), cos(x)")
show()

#______-diagrama Hertzsprung-Russell . Magnitudvs temperatura de estrellas
from pylab import scatter,xlabel,ylabel,xlim
from numpy import loadtxt

data= loadtxt("stars.txt",float)

x= data[:,0]
y= data[:,1]

scatter(x,y)
xlabel("Temperatura")
ylabel("Magnitud")
xlim(0,13000)
ylim(-5,20)
show()

#_______________________Density plots a two dimensional plot___HEAT MAPS
from pylab import imshow,gray
#rojo es frio, azul es caliente
data = loadtxt("circular.txt",float)
imshow(data,origin="lower")  # imshow convierte a datos interpretados por colores #lower baja el origen
#gray()   #convierte a grises  
show()

