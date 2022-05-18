from tkinter.font import BOLD
import PP_library as lib
import matplotlib.pyplot as plt

data = lib.loadList('RigelB_RV.csv')

timeList = []
primList = []
secList = []
unknownList = []
for n in range(len(data)):
    time = data[n][0]
    prim = data[n][1]
    sec = data[n][2]
    unknown = data[n][3]
    if time != '' and prim != '':
        timeList.append(float(time))
        primList.append(float(prim))
    if time != '' and sec != '':
        timeList.append(float(time))
        secList.append(float(sec))
    if time != '' and unknown != '':
        timeList.append(float(time))
        unknownList.append(float(unknown))

cList = []
x = timeList
correlatedList = []
for n in range(len(primList)):
    correlatedList += [primList[n],secList[n]]
    cList += ['blue','red']
y = correlatedList + unknownList
cList += ['blue','blue','blue','blue','blue']
plt.scatter(x,y,10,cList)
plt.suptitle('Radial Velocity for Rigel Ba and Bb Binary',fontweight=BOLD)
plt.title('From American Astronomical Society $\it{(1942)}$')
plt.xlabel('Time (Days)')
plt.ylabel('Radial Velocity (km/s)')
plt.grid(True)
plt.axhline(y=19.1,color='k',linestyle='dashed',linewidth=1.5)
plt.axvline(x=0,color='orange',linestyle='dashed',linewidth=1)
plt.axvline(x=9.86,color='orange',linestyle='dashed',linewidth=1)
plt.annotate('19.1 km/s',(8,15),color='k')
plt.annotate('Period Range',(0,-18),color='orange')
plt.show()