#:)

from vpython import *


escena = canvas(width=1200,height=600)
escena.title = "ANIMACION 3D ITI Mecatronica 2do sem"

grav = vector(0,-10,0)
bola = sphere(pos=vector(0,5,0), radius=1, color=color.green)
suelo = box(size=vector(8,0.1,8),pos=vector(0,-1,0),color=color.red)

bola.vel= vector(0,0,0)
dt= 0.01
t=0

while 1:
    t += dt
    bola.vel += grav * dt
    bola.pos += bola.vel * dt
    if bola.pos.y < 0:
        bola.vel *= -1
        bola.pos.y=0
    rate(100)
    #Rate es numero de frames por segundo, junto con dt podemos observar
    #en tiempo real