#____________-TIRO PARABOLICO

from vpython import *
from vpython import graph
import time
#_________-ajustando la pantalla para la escena
escena = canvas(width=800,height=500)
escena.title = "Tiro Parabolico ITI Mecatronica 2do sem"
escena.background=color.white
escena.center=vector(0,2,0)

#______________________Agregando un grafico
"""El siguiente grafico mostrara la evolucion de la energia cinetica, potencial y total a lo 
largo del tiempo en que la esfera es expulsada y toca el suelo"""
graph1= graph(x=0,y=0,width=500,height=350,title="Energia vs tiempo",
                xtitle='t',ytitle='E',foreground=color.black,
                 background=color.white)

potencial= gcurve(graph=graph1,color=color.blue)
cinetica = gcurve(graph=graph1,color=color.red)
etotal = gcurve(graph=graph1,color=color.green)

#_________________determinando vectores y variables
pos = vector(-10,0,0)
vel = vector(10,10,0)   #vectores de poscicion y velocidad

grav = 10  #gravedad
m=1
acel = vector(0,-grav,0)  #aceleracion
dt = 1./50.  #derivada del tiempo
t= 0 #tiempo en cero
#________________________Definiendo objetos
proyectil = sphere(pos=pos,color=color.blue,radius=0.5)
suelo = box(pos=vector(0,-1,0),size=vector(25,0.1,25),color=color.red)
cannon = cylinder(pos=pos,axis=vector(1,1,0))
trayectoria = curve(color=color.white)

velocidad_total = arrow(color=color.red,pos=proyectil.pos,axis=vel/3.)
velocidad_x = arrow(color=color.green,pos=proyectil.pos,axis=vector(vel.x/3.,0,0))
velocidad_y = arrow(color=color.green,pos=proyectil.pos,axis=vector(0,vel.y/3.,0))

#____________________Definiendo la fisica del movimiento en el entorno
time.sleep(5)
while pos.y >= 0:
    vel= vel + acel*dt
    pos = pos + vel*dt
    trayectoria.append(pos)
    proyectil.pos = pos
    velocidad_total.pos = pos
    velocidad_x.pos = pos
    velocidad_y.pos = pos
    velocidad_total.axis=vel/3.
    velocidad_x.axis=vector(vel.x/3.,0,0)
    velocidad_y.axis=vector(0,vel.y/3.,0)
    #Agregando puntos a la gráfica
    cinetica.plot(pos=(t,0.5 * m * mag2(vel)))
    potencial.plot(pos=(t,m * grav * proyectil.pos.y))
    etotal.plot(pos=(t,m * grav * proyectil.pos.y + 0.5 * m * mag2(vel)))
    t = t + dt
    rate(50) #frames por segundo 


    
