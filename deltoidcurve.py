#graphics cap3
#plotting a deloid curve

import math
import matplotlib.pyplot as plt
from matplotlib import style
#"deltoids curve"
style.use("ggplot")

tetha = 0.0
tetha_2 = float(2*math.pi)
total = tetha_2/100
xs = []
ys = []
for i in range(101):
    xs.append(2*math.cos(tetha) + math.cos(2*tetha))
    ys.append(2*math.sin(tetha) - math.sin(2*tetha))
    tetha += total
print(xs,"\n")
print(ys)
try:
    plt.title("Deltoids curve")
    
    plt.plot(xs,ys,'g--',label="parametric curve")
    plt.ylabel("f(x)")
    plt.xlabel("x")
    plt.legend(loc=4)
    plt.show()
except Exception as e:
    print(str(e))
    pass
finally:
    plt.show()