#Cluster_Number,Number_in_cluster,UBV_source_num,B-V_Mag,V_Mag,Lum_Class,Log_Temp(K),Log_lum(Sun),Age(yr),Mass (Sun),Prob(Age/mass)
import PP_library as lib
import math
import matplotlib.pyplot as plt

data = lib.loadList('stellar_data#4.csv')

lumList = []
massList = []
cList = []
for n in range(len(data)):
    luminosity_log = data[n][7]
    mass = data[n][9]
    lumClass = float(data[n][5])
    if luminosity_log != '' and mass != '':
        lumList.append(float(luminosity_log))
        mass_log = math.log10(float(mass))
        massList.append(mass_log)
        if lumClass == 5:
            cList.append('r')
        else:
            cList.append('y')

x = massList
y = lumList
c = cList
plt.scatter(x,y,1,c)
plt.title('Luminosity vs. Mass Relation',fontweight='bold')
plt.xlabel('Log of Solar Masses')
plt.ylabel('Log of Solar Luminosities')
plt.grid(True)
plt.show()