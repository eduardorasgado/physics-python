#Derivadas y tangentes
from numpy import sin,linspace,power
from pylab import plot, show,title

def f(x):
    return x*sin(power(x,2))  #cambiar por su funcion

#evaluation of the function
x = linspace(-2,4,150) #desde -2 hasta 4 en 150 particiones
y = f(x)

#derivada en un punto dado
a = 1.4
h = 0.1

#derivada
fprime = (f(a+h)-f(a))/h #derivative
tan = f(a) + fprime*(x-a) #tangent

#plot of the function and the tangent
plot(x,y,"b",a,f(a),"om",x,tan,'r--')
title("$xsin(x^2)$")
show()