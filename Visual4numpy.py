#___________________________-METODOS NUMERICOS CAPITULO 2
#PROGRAMINGCAP2

#slicing con arrays
from numpy import array
a = array([2,4,6,8,10,12,14,16],int)
b= a[3:6]
print(b,"\n")

#ciclos for

for n in range(20,2,-3):
    print(n)

print("\n")
p = 10
q = 2
for n in range(p//q):
    print((p+q)**n)
    
#usando arange__-genera un arreglo unidimencional
from numpy import arange
b = arange(0,8,2) #even
print("\n",b)
g = arange(1,10,2) #ood
print(g)
t = arange(2.0,2.8,0.2) #floats
print(t)

#usando linspace de numpy____genera un aggreglo entre dos numeros y los parte entre un tercero
from numpy import linspace

lin = linspace(2.0,3.0,10)#esto partido en diez partes
print("\n",lin)

#sumatorias_____________________
#suma de k=1 a n=100 de 1/k
s=0.0
for k in range(1,101):
    s += 1/k
print("\n",s)

#__________factoriales de un numero
j = 0
def Factorial(n):
    f=1.0
    for i in range(1,n+1):
        f *= i
    return f

k = Factorial(6)
print(k)

#calculando la distancia entre un cilindro y el centro del espacio3d:
from math import sin,cos,sqrt

def distancia(r,theta,z):
    x= r*cos(theta)
    y=r*sin(theta)
    d=sqrt(x**2+y**2+z**2)
    return d

dis_cyl = distancia(2.0,0.1,-1.5)
print("La distancia entre el centro del cilindro y el origen es de: ",dis_cyl,"\n")

#Funcion para convertir coordenadas polares a cartesianas
def cartesiana(r,theta):
    x=r*cos(theta)
    y=r*sin(theta)
    return array([x,y],float)

antes_polares = cartesiana(2.5,0.1)
print("La coordenada polar dada es en cartesiana: ", antes_polares)


input("Press enter")