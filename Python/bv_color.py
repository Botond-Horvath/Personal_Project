#Cluster_Number,Number_in_cluster,UBV_source_num,B-V_Mag,V_Mag,Lum_Class,Log_Temp(K),Log_lum(Sun),Age(yr),Mass(Sun),Prob(Age/mass)
import math
import PP_library as lib
import matplotlib.pyplot as plt

data = lib.loadList('stellar_data#4.csv')

cList = []
def findColor(cluster,lumClass):
    if cluster <= 10 and lumClass == 5:
        cList.append('blue')
    elif cluster > 10 and cluster <= 20 and lumClass == 5:
        cList.append('white')
    elif cluster > 20 and cluster <= 30 and lumClass == 5:
        cList.append('green')
    elif cluster > 30 and cluster <= 40 and lumClass == 5:
        cList.append('yellow')
    elif cluster > 40 and cluster <= 50 and lumClass == 5:
        cList.append('orange')
    elif cluster > 50 and lumClass == 5:
        cList.append('red')
    else:
        cList.append('black')

bvList = []
tempList = []
myList = []
for n in range(len(data)):
    bvMag = data[n][3]
    temp_log = data[n][6]
    cluster = float(data[n][0])
    lumClass = float(data[n][5])
    if bvMag != '' and temp_log != '':
        bvMag = float(bvMag)
        temp = 10**(float(temp_log))
        bvList.append(bvMag)
        tempList.append(temp)
        myList.append(lumClass)
        findColor(cluster,lumClass)

x = bvList
y = tempList
c = cList
plt.scatter(x,y,1,c)
plt.title('Star Temperature vs. B-V Magnitude',fontweight='bold')
plt.xlabel('B-V Magnitude of Star')
plt.ylabel('Temperature of Star (K)')
plt.ylim(0,30000)
plt.grid(True)
plt.show()

