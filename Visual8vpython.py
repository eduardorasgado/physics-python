#___________________________________Graphics chapter 3
#3D GRAPHICS__using vpython and others

from vpython import *
ecena = canvas(width=800,height=800)
ecena.title="Esfera"
ecena.center=vector(0,0,0)
sand = sphere(radius=1.0,pos=vector(0,5,0),color=color.cyan)
floor = box(pos=vector(0,-1,0),size=vector(26,0.05,26),color=color.white)  # x,y,z

gravedad = vector(0,-10,0)
sand.vel = vector(0,0,0)
dt= 0.01
t = 0
while t<30:
    t += dt
    sand.vel += gravedad * dt
    sand.pos += sand.vel *dt
    sand.pos.x +=0.01
    
    if sand.pos.y < 0:
        sand.vel *= -1
        sand.pos.y = 0
        
        
    rate(100)
