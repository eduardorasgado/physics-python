#min from function
import numpy
import pylab
from scipy.optimize import fmin

#objetive function
rsinc = lambda x: -1*numpy.sin(x)/x

x0 = -5 #start from x= -5
xmin0 = fmin(rsinc,x0)  #la funcion obtiene el punto x que representa al minimo

x1 = -4 #start from x=-4
xmin1 = fmin(rsinc,x1)

#comprobamos el punto minimo
y0 = rsinc(xmin0)
y1 = rsinc(xmin1)
#elegimos el minimo correcto
compare = [y0,y1]
compare.sort()
#ordenar de menor a mayor
print(compare)
verif = (compare[0] == y0) #si y0 el punto es xmin0
verif2 = (compare[0]== y1) #si y1 el punto es xmin1 

if verif:
    minx = xmin0
    miny = compare[0]
elif verif2:
    minx = xmin1
    miny = compare[0]

#plot the function
x =numpy.linspace(-15,15,100)
y = rsinc(x)
pylab.plot(x,y)
#plot of x correct and its minimum
pylab.plot(minx,miny,'ro',label="minimo: x= {},y={}".format(minx,miny))

pylab.axis([-15,15,-1.3,0.3]) #ejes del plano
pylab.legend(loc=4)
pylab.title('$-1 sin(x)/x$')
pylab.show()


#Solo buscando desde -4 encontramos el minimo global, con -5 se atasca en un minimo local