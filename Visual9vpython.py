#________________________CHAPTER 3:GRAPHICS PROCESSING

from vpython import sphere
from vpython import *

L = 5
R = 0.3

for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
            sphere(pos=vector(i,j,k),radius=R,color=color.red)
            
#ctrl + mouse para mover la escena
#GRAPHICSCAP3 PAG 26
    