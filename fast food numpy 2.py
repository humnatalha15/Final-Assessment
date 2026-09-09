import numpy as np
lon, lat=np.genfromtxt('FastFoodRestaurants (1).csv', delimiter=',', usecols=(4,5), unpack=True, dtype=float, invalid_raise=False)
valid=~np.isnan(lon) & ~np.isnan(lat)
lon=lon[valid]
lat=lat[valid]
print(lon)
print(lat)
print(np.min(lat))
print( np.mean(lat))
print( np.average(lat))
print( np.std(lat))
print( np.median(lat))
print( np.percentile(lat,25))
print( np.percentile(lat,75))
print( np.percentile(lat,3))
print( np.min(lat))
print( np.max(lat))
print(np.square(lat))
print( np.sqrt(lat))
print( np.power(lat,lat))
print( np.abs(lat))
addition = lat+lon
subtraction = lat - lon
multiplication = lat* lon
division = lat / lon

print( addition)
print( subtraction)
print( multiplication)
print(division)
latPie = (lat/np.pi) +1
sine_values = np.sin(latPie)
cosine_values = np.cos(latPie)
tangent_values = np.tan(latPie)

print( sine_values)
print( cosine_values)
print(tangent_values)
log_array = np.log(np.abs(latPie))
log10_array = np.log10(np.abs(latPie))

print(log_array)
print( log10_array)
D2lonlat = np.array([lon,lat])
print(D2lonlat)
print(D2lonlat.ndim)
print(D2lonlat.size)
print(D2lonlat.shape)
print(D2lonlat.dtype)
D2lonlatslice=D2lonlat[0:1:1, 1:5:1]
print(D2lonlatslice)
D2lonlatslice=  D2lonlat[:1, 4:15:4]
print(D2lonlatslice)
D2lonlatsliceItemonly=D2lonlatslice[0,1]
print(D2lonlatsliceItemonly)
D2lonlatslice2Itemonly=D2lonlatslice[0,2]
print(D2lonlatslice2Itemonly)
for elem in np.nditer(D2lonlat):
    print(elem)
for index, elem in np.ndenumerate(D2lonlat):
    print(index, elem)
D2lonlat1T019812 = np.reshape(D2lonlat, (1, 19812))
print(D2lonlat1T019812 )
print(D2lonlat1T019812.size)
print( D2lonlat1T019812.ndim)
print( D2lonlat1T019812.shape)
print(D2lonlat1T019812.ndim)