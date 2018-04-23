from vpython import *

escena = canvas()
escena.title = "formas con visual python"
caja = box(pos=vector(4,2,3),size=vector(8.,4.,6.),color=color.red)
bola = sphere(pos=vector(4,7,3),radius=2,color=color.green)

bola.masa=1

bola.vel=vector(0,-1,0)

a = vector(1.,2.,3.)
b=vector(4.,5.,6.)

c = a+b
d=3.5*a
e=dot(a,b)
f=cross(a,b)
g=norm(a)

t=0
dt=0.001
while t<100:
    t=t+dt
    bola.vel=bola.acel*dt
    bola.pos=bola.vel*dt