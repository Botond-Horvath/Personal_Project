import PP_library as lib
from matplotlib import pyplot as plt

data = lib.loadList('51peg_RVdata.csv')

#BJD,RV (m/s),RV Err (m/s),Inst (Automated Planet Finder at Lick Obs. in California)
col = {'BJD':0,'RV':1,'Err':2,'Inst':3}

rvList = []
dateList = []
for n in range(len(data)):
    radial_velocity = data[n][col['RV']]
    date = data[n][col['BJD']]
    rvList.append(float(radial_velocity))
    dateList.append(float(date))

print(dateList)
print('Maximum date: ' + str(max(dateList)))
print('Minimum date: ' + str(min(dateList)))

plt.title('Radial Velocity of 51-Pegasi \nover Observations Time')
plt.xlabel('Barycentric Julian Days')
plt.ylabel('Radial Velocity (m/s)')
plt.scatter(dateList,rvList,s=10)
plt.show()
