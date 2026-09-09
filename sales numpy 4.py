import numpy as np
sale_amount, assessed_value= np.genfromtxt('Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',', skip_header=1, usecols=(5,6), unpack=True, dtype=float, invalid_raise=False)
print(sale_amount)
print(assessed_value)
print(np.min(sale_amount))
print( np.mean(sale_amount))
print( np.average(sale_amount))
print( np.std(sale_amount))
print( np.median(sale_amount))
print( np.percentile(sale_amount,25))
print( np.percentile(sale_amount,75))
print( np.percentile(sale_amount,3))
print( np.min(sale_amount))
print( np.max(sale_amount))
print(np.square(sale_amount))
print( np.sqrt(sale_amount))
print( np.power(sale_amount,assessed_value))
print( np.abs(sale_amount))
addition = sale_amount+assessed_value
subtraction = sale_amount - assessed_value
multiplication = sale_amount* assessed_value
division = sale_amount / assessed_value

print( addition)
print( subtraction)
print( multiplication)
print(division)
sale_amountPie = (sale_amount/np.pi) +1
sine_values = np.sin(sale_amountPie)
cosine_values = np.cos(sale_amountPie)
tangent_values = np.tan(sale_amountPie)

print( sine_values)
print( cosine_values)
print(tangent_values)
log_array = np.log(np.abs(sale_amountPie))
log10_array = np.log10(np.abs(sale_amountPie))

print(log_array)
print( log10_array)
D2sale_amountassessed_value= np.array([sale_amount,assessed_value])
print(D2sale_amountassessed_value)
print(D2sale_amountassessed_value.ndim)
print(D2sale_amountassessed_value.size)
print(D2sale_amountassessed_value.shape)
print(D2sale_amountassessed_value.dtype)
D2sale_amountassessed_valueslice=D2sale_amountassessed_value[0:1:1, 1:5:1]
print(D2sale_amountassessed_valueslice)
D2sale_amountassessed_valueslice=  D2sale_amountassessed_value[:1, 4:15:4]
print(D2sale_amountassessed_valueslice)
D2sale_amountassessed_valuesliceItemonly=D2sale_amountassessed_valueslice[0,1]
print(D2sale_amountassessed_valuesliceItemonly)
D2sale_amountassessed_valueslice2Itemonly=D2sale_amountassessed_valueslice[0,2]
print(D2sale_amountassessed_valueslice2Itemonly)
for elem in np.nditer(D2sale_amountassessed_value):
    print(elem)
for index, elem in np.ndenumerate(D2sale_amountassessed_value):
    print(index, elem)
D2sale_amountassessed_value1T0278 = np.reshape(D2sale_amountassessed_value, (1, 278))
print(D2sale_amountassessed_value1T0278) 
print(D2sale_amountassessed_value1T0278.size)
print( D2sale_amountassessed_value1T0278.ndim)
print( D2sale_amountassessed_value1T0278.shape)
print(D2sale_amountassessed_value1T0278.ndim)