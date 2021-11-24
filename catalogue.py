import PP_library
import math
pi = math.pi

data = PP_library.loadList("PP_exoplanet.csv")

#PlanetIdentifier,TypeFlag,PlanetaryMassJpt,RadiusJpt,PeriodDays,SemiMajorAxisAU,Eccentricity,PeriastronDeg,LongitudeDeg,AscendingNodeDeg,InclinationDeg,SurfaceTempK,AgeGyr,DiscoveryMethod,DiscoveryYear,LastUpdated,RightAscension,Declination,DistFromSunParsec,HostStarMassSlrMass,HostStarRadiusSlrRad,HostStarMetallicity,HostStarTempK,HostStarAgeGyr
col = {'name':0,'massJpt':2,'radiusJpt':3,'periodDays':4,'smaAU':5,'ecc':6,'tempK':11,'ageB':12,'method':13,'year':14,'RA':16,'D':17,'stMassSolar':19,'stRadSolar':20,'stMt':21,'stTempK':22,'stAgeB':23}

def stringConverter(string):
    string = string.lower()
    string = string.replace(' ','')
    string = string.replace('-','')
    return string

def check(parameter):
    if parameter == "":
        parameter = "unknown"
    else:
        parameter = round(float(parameter),2)
        parameter = (str(parameter) + unit)
    return parameter

def checkUnit(mass,radius):
    massUnit = ' jupiters'
    radiusUnit = ' jupiters'
    if mass != '':
        mass = float(mass)
        if mass < 0.1:
            mass /= earthMass
            massUnit = ' earths'
    if radius != '':
        radius = float(radius)
        if radius < 0.25:
            radius /= earthRadius
            radiusUnit = ' earths'
    unitList = [massUnit, radiusUnit, mass, radius]
    return unitList

def calcDensity(mass, radius):
    density = ''
    if mass != '' and radius != '':
        mass = float(mass)
        radius = float(radius)
        mass *= (1.898 * 10**30)
        radius *= 6991100000
        density = mass / (4/3*(pi*radius**3))
        density = round(density,2)
    return density

def calcClass(t):
    if t != '':
        t = int(t)
        if t >= 30000:
            starClass = ' (O-type)'
        elif t >= 10000 and t < 30000:
            starClass = ' (B-type)'
        elif t >= 7500 and t < 10000:
            starClass = ' (A-type)'
        elif t  >= 6200 and t < 7500:
            starClass = ' (F-type)'
        elif t >= 5400 and t < 6200:
            starClass = ' (G-type)'
        elif t >= 4000 and t < 5400:
            starClass = ' (K-type)'
        else:
            starClass = ' (M-type)'
    return starClass

earthRadius = 0.089
earthMass = 0.003

exoplanet = str(input("Please enter the name of the exoplanet that you want info on: \n"))
exoplanetConverted = stringConverter(exoplanet)

for n in range(0,len(data)):
    name = data[n][col['name']]
    nameConverted = stringConverter(name)
    if nameConverted == exoplanetConverted:
        planet = name
        index = n

print("Ok, here is all of the information that we know for " + planet + " :")

mass = data[index][col['massJpt']]
radius = data[index][col['radiusJpt']]
unitList = checkUnit(mass,radius)
unit = unitList[0]
mass = unitList[2]
mass = check(mass)
unit = unitList[1]
radius = unitList[3]
radius = check(radius)

unit = 'g/cm^3'
density = calcDensity(data[index][col['massJpt']], data[index][col['radiusJpt']])
density = check(density)

unit = ' days' 
period = check(data[index][col['periodDays']])

unit = 'AU'
sma = check(data[index][col['smaAU']])

unit = ''
eccentricity = check(data[index][col['ecc']])

unit = ' kelvins'
temperature = check(data[index][col['tempK']])

discoveryMethod = data[index][col['method']]
discoveryYear = data[index][col['year']]

print("MASS: " + mass)
print("RADIUS: " + radius)
print("DENSITY: " + str(density))
print("PERIOD: " + period)
print("SEMI-MAJOR-AXIS: " + sma)
print("ECCENTRICITY: " + eccentricity)
print("TEMPERATURE: " + temperature)
print("METHOD OF DETECTION: " + discoveryMethod)
print("YEAR OF DISCOVERY: " + discoveryYear)

print("Below is all of the infromation that we know of the star of "+ planet + ": ")

unit = ' solar masses'
mass = check(data[index][col['stMassSolar']])

unit = ' solar radii'
radius = check(data[index][col['stRadSolar']])

unit = ''
metallicity = check(data[index][col['stMt']])

unit = ' kelvins'
temperature = check(data[index][col['stTempK']])
starClass = calcClass(data[index][col['stTempK']])

unit = ' Ga'
age = check(data[index][col['stAgeB']])

print("MASS: " + mass)
print("RADIUS: " + radius)
print("METALLICITY: " + metallicity)
print("TEMPERATURE: " + temperature + starClass)
print("AGE: " + age)
