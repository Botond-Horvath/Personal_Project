#Temperature (K),Luminosity(L/Lo),Radius(R/Ro),Absolute magnitude(Mv),Star type,Star color,Spectral Class
import PP_library as lib
import matplotlib.pyplot as plt
import math

data = lib.loadList('stellar_data#2.csv')

lumList = []
radList = []
cList = []
for n in range(len(data)):
    luminosity = float(data[n][1])
    radius = float(data[n][2])
    type = float(data[n][4])
    if luminosity != '' and radius != '':
        logLum = math.log(luminosity,10)
        logRad = math.log(radius,10)
        lumList.append(logLum)
        radList.append(logRad)
        if type == 3:
            color = 'y'
        elif type > 3:
            color = 'b'
        else:
            color = 'r'
        cList.append(color)

x = radList
y = lumList
c = cList
plt.scatter(x,y,10,c)
plt.title('Stellar Luminosity vs. Radius',fontweight='bold')
plt.xlabel('Log of Radius (Solar)')
plt.ylabel('Log of Luminosity (Solar)')
plt.grid(True)
plt.annotate('Dwarfs',(-0.1,-4),color='red')
plt.annotate('Main Sequence (V)',(-1,2.5),color='yellow')
plt.annotate('Giants (IV,III,II,Ia/b)',(1.5,4.1),color='blue')
plt.show()


