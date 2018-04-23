#Visual dos brazo mecatronico
from vpython import *

scene = canvas()
scene.title = "Péndulo Inercial. Mecánica y cinemática. Mecatrónica, ITI 2017"
scene.autoscale = 0
#definiendo las dimenciones del trompo
l1= 0.7
l2 = 5
l3 = 12.5
#coeficiente de relacion de frecuencia de paralepipedo recto:
coef = ((13**2-12**2)/(13*2+12*2))**(-0.5)
dim = 13*3/4 #proporcion estetica

phi0=2

#Sistema de referencia en rotacion
SRR= frame(pos=vector(0,0,0))

#Sistema de referencia del trompo
SRP = frame(frame=SRR)

#Ejes de soporte
ejes= curve(pos=[vector(dim*3/4,0,0),vector(0,0,0),vector(0,dim*3/4,0),vector(0,0,0),
                vector(0,0,dim*3/4)],color=color.blue)
Soporte1= box(frame=SRR,pos=[0,-dim,0],size=[dim,0.5,dim],color=color.green)
Soporte2= box(frame=SRR,pos=[dim/2,-dim/2,0],size=[0.5,dim,0.5],color=color.green)
Soporte3 = box(frame=SRR,pos=[-dim/2,-dim/2,0],size=[0.5,dim,0.5],color=color.green)
Eje = cylinder(frame=SRR,pos=[-dim/2,0,0],axis=[dim,0,0],radius=0.2,color=color.green)

#Definimos dos bolas como marcadores(sin sentido fisico)
bola1= sphere(frame=SRP,pos=[0,13/2,0])
bola2= sphere(frame=SRP,pos=[0,-13/2,0])
bola1.radius=0.5
bola1.color=color.red
bola2.radius=0.5
bola2.color=color.blue

#El trompo

top= box(frame=SRP,pos=vector(0,0,0),size=vector(l2,l3,l1),axis=vector(0,0,l3),color=color.blue)

omega=1.
dt=0.02
phi=pi/2-phi0
phip=0
phipp=omega**2.*coef*sin(2.*phi)/2.
SRP.rotate(frame=SRR,axis=(-1,0,0),angle=phi)

