#JD,Phase,Rad.Vel. (km/s),Component

import PP_library as lib
import matplotlib.pyplot as plt

data = lib.loadList('AB_Andromedae_RV.csv')

phaseList = []
RVList = []
cList = []
for n in range(len(data)):
    phase = float(data[n][1])
    RV = float(data[n][2])
    comp = data[n][3]
    phaseList.append(phase)
    RVList.append(RV)
    if comp == 'a':
        cList.append('r')
    else:
        cList.append('g')

x = phaseList
y = RVList
plt.scatter(x,y,10,cList)
plt.title('Radial Velocity of AB Andromedae (A contact binary)',fontweight='bold')
plt.xlabel('Phase (in range of JD data)',fontweight='bold')
plt.ylabel('Radial Velocity (km/s)',fontweight='bold')
plt.ylim(-300,250)
plt.axhline(y=-27.53,color='k',linestyle='dashed',linewidth=1.5)
plt.annotate('-27.53 km/s',(0,-50),color='black')
plt.grid(True)
plt.show()

