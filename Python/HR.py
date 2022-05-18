#id,hip,hd,hr,gl,bf,proper,ra,dec,distance,pmra,pmdec,rv,appMag,absMag,spectral_type,b-v,x,y,z,vx,vy,vz,rarad,decrad,pmrarad,pmdecrad,bayer,flam,con,comp,comp_primary,base,lum,var,var_min,var_max
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import PP_library
import math

data = PP_library.loadList('stellar_data#3.csv')

col = {'distance':9,'magApp':13,'magAbs':14,'typeS':15,'b-v':16}

def findRad(lum,index):
    if index != '':
        index = float(index)
        temp = 4600*((1/(0.92*index+1.7))+(1/(0.92*index+0.62)))
        tempSolar = temp / 5778
        rad = (math.sqrt(lum))/(tempSolar**2)
        return(rad)

def findLum(magAbs):
    magAbs = float(magAbs)
    dif = 4.83 - magAbs
    lum = 2.512**dif
    lum = round(lum,4)
    return(lum)

colorList = []
lumList = []
cList = []
sList = []
for n in range(len(data)):
    color = data[n][col['b-v']]
    luminosity = findLum(data[n][col['magAbs']])
    if color != '':
        color = float(color)
        colorList.append(color)
        lumList.append(luminosity)
        if color < 0.7 and luminosity < 10**-2:
            cList.append('#FFFFFF')
        elif color >= 1.6:
            cList.append('#FA0707')
        elif color < 1.6 and color >= 1.2:
            cList.append('#FA5F07')
        elif color < 1.2 and color >= 0.6:
            cList.append('y')
        elif color < 0.6 and color >= 0:
            cList.append('#05F7E8')
        else:
            cList.append('#05A6F7')
        rad = findRad(luminosity, data[n][col['b-v']])
        sList.append(rad)

#Plot 1 without size
x = colorList
y = lumList
plt.yscale('log')
plt.scatter(x,y,0.5,cList)
plt.title('Hertzsprung-Russell Diagram',fontweight='bold',fontsize=15)
plt.xlabel('B-V Color Magnitude')
plt.xlim(-0.5,2)
plt.ylabel('Solar Luminosity')
plt.ylim(10**-4.5,10**8)
plt.annotate('White Dwarfs',(-0.4,10**-4),color='white')
plt.annotate('Main Sequence (V)',(0.6,10**-2.8),color='yellow')
plt.annotate('Giants (IV,III,II)',(1.4,10**-0.4),color='orange')
plt.annotate('Supergiants (Ia, Ib)',(1,10**4.5),color='orange')

ax = plt.gca()
ax.set_facecolor('xkcd:black')
plt.show()

#Plot 2 with size
x = colorList
y = lumList
plt.yscale('log')
plt.scatter(x,y,sList,cList)
plt.title('Hertzsprung-Russell Diagram (Size to Scale)',fontweight='bold',fontsize=15)
plt.xlabel('B-V Color Magnitude')
plt.xlim(-0.5,2)
plt.ylabel('Solar Luminosity')
plt.ylim(10**-4.5,10**9)
ax = plt.gca()
ax.set_facecolor('xkcd:black')
plt.show()
