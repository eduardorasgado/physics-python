#__________________________METODOS NUMERICOS:USO DE NUMPY Y MATH;PROGRAMMING CAP 2
#__CAPITULO 2
from numpy import zeros


a = zeros(4,float)
print(a,"\n")

#arreglo de dos dimensiones de n y m filas y columnas: zeros([m,n],float)
b = zeros([3,4],float)
print(b,"\n")

r = [1.0,1.5,-2.2]
promedio = sum(r)/len(r)
print(promedio)

#_________
from math import log
d = [1.0,1.5,2.2]
logd = list(map(log,d))
print("\n",logd)

#arrays
from numpy import array
a= array([[0,1,2],[4,5,6]],float)
print("\n",a)
f=list(a)
print("\n",f)

#de nuevo con zeros

i = zeros([4,4],int)
i[0,0] = 1
i[1,1] = 1
i[2,2] = 1
i[3,3] = 1

print("\n", i)

#___Arrays
a = array([1,2,3,4],int)
b=2*a
print("\n",b)
print("\n",a+b)
#vector por un escalar:

suma = a+b
print("\n",suma*4)

#____________________________PRODUCTO DE VECTORES

from numpy import dot
vector1 = array([1,2,3,4],int)
vector2 = array([5,7,8,9],int)
print("\n",dot(a,b))

#________Multiplicador de MATRICES DE 2X2

matriz1 = array([[1,3],[2,4]],int)
matriz2 = array([[4,-2],[-3,1]],int)
matriz3 = array([[1,2],[2,1]],int)

#multiplicacion de las primeras matriz1 y 2 y suma del producto de 2 x matriz3
resultado = dot(matriz1,matriz2)+(2*matriz3)
print("\n",resultado)
#otro ejemplo:
matriz4= array([[2,0],[4,1]],int)
matriz5 = array([[3,1],[4,2]],int)

print("\n",dot(matriz4,matriz5))

#_____________ obtener tamaño y forma de matriz

a = array([[1,2,3],[5,6,7],[8,9,0]],int)
print("\n", a)
print(a.size) #imprime el numero de miembros del arreglo
print(a.shape) #imprime el orden de la matriz

"""
#El promedio de un conjunto de valores dados dentro de un archivo txt
from numpy import loadtxt
values = loadtxt("values.txt",float)
mean = sum(values)/len(values)
print(mean)
"""
"""
#mas pro: programmingcap2 pag 55
from numpy import loadtxt, log
from math import exp
values = loadtxt("values.txt",float)
geometric = exp(sum(log(values))/len(logs))
print(geometric)

"""
#_______copiando arrays en nueva variable(asi nomas no es posible)
from numpy import copy
a= array([3,4,6,5],int)
b=copy(a)
a[2]= 0
print("\n",a)
print("\n",b)


input("Press a key")