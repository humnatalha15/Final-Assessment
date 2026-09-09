import numpy as np
price,bed,bath,acre_lot=np.genfromtxt('RealEstate-USA (1).csv', delimiter=',',usecols=(0,4,8,9),unpack=True, dtype=None, skip_header=1)
print(price)
print(bed)
print(bath)
print(acre_lot)
print(np.min(price))
print( np.mean(price))
print( np.average(price))
print( np.std(price))
print( np.median(price))
print( np.percentile(price,25))
print( np.percentile(price,75))
print( np.percentile(price,3))
print( np.min(price))
print( np.max(price))
print(np.square(price))
print( np.sqrt(price))
print( np.power(price,price))
print( np.abs(price))
addition = price+ acre_lot
subtraction = price - acre_lot
multiplication = acre_lot* price
division = acre_lot / price

print( addition)
print( subtraction)
print( multiplication)
print(division)
pricePie = (price/np.pi) +1
sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)

print( sine_values)
print( cosine_values)
print(tangent_values)
log_array = np.log(pricePie)
log10_array = np.log10(pricePie)

print(log_array)
print( log10_array)

D2priceAcre_lot = np.array([price,acre_lot])
print(D2priceAcre_lot)
print(D2priceAcre_lot.ndim)
print(D2priceAcre_lot.size)
print(D2priceAcre_lot.shape)
print(D2priceAcre_lot.dtype)
D2priceAcre_lotslice=D2priceAcre_lot[0:1:1, 1:5:1]
print(D2priceAcre_lotslice)
D2priceAcre_lotslice=  D2priceAcre_lot[:1, 4:15:4]
print(D2priceAcre_lotslice)
D2priceAcre_lotsliceItemonly=D2priceAcre_lotslice[0,1]
print(D2priceAcre_lotsliceItemonly)
D2priceAcre_lotslice2Itemonly=D2priceAcre_lotslice[0,2]
print(D2priceAcre_lotslice2Itemonly)
for elem in np.nditer(D2priceAcre_lot):
    print(elem)


for index, elem in np.ndenumerate(D2priceAcre_lot):
    print(index, elem)
D2priceAcre_lot1TO400 = np.reshape(D2priceAcre_lot, (1, 400))
print( D2priceAcre_lot1TO400)
print(D2priceAcre_lot1TO400.size)
print( D2priceAcre_lot1TO400.ndim)
print( D2priceAcre_lot1TO400.shape)
print(D2priceAcre_lot1TO400.ndim)




print()