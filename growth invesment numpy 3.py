import numpy as np
investment, valuation= np.genfromtxt('startup_growth_investment_data.csv', delimiter=',',skip_header=1, usecols=(3,4),unpack=True, dtype=float)
print(investment)
print(valuation)
print(np.min(investment))
print( np.mean(investment))
print( np.average(investment))
print( np.std(investment))
print( np.median(investment))
print( np.percentile(investment,25))
print( np.percentile(investment,75))
print( np.percentile(investment,3))
print( np.min(investment))
print( np.max(investment))
print(np.square(investment))
print( np.sqrt(investment))
print( np.power(investment,valuation))
print( np.abs(investment))
addition = investment+valuation
subtraction = investment- valuation
multiplication = investment* valuation
division = investment / valuation

print( addition)
print( subtraction)
print(multiplication)
print(division)
investmentPie = (investment/np.pi) +1
sine_values = np.sin(investmentPie)
cosine_values = np.cos(investmentPie)
tangent_values = np.tan(investmentPie)

print( sine_values)
print( cosine_values)
print(tangent_values)
log_array = np.log(np.abs(investmentPie))
log10_array = np.log10(np.abs(investmentPie))

print(log_array)
print( log10_array)
D2investmentvaluation = np.array([investment,valuation])
print(D2investmentvaluation)
print(D2investmentvaluation.ndim)
print(D2investmentvaluation.size)
print(D2investmentvaluation.shape)
print(D2investmentvaluation.dtype)
D2investmentvaluationslice=D2investmentvaluation[0:1:1, 1:5:1]
print(D2investmentvaluationslice)
D2investmentvaluationslice=D2investmentvaluation[:1, 4:15:4]
print(D2investmentvaluationslice)
D2investmentvaluationItemonly=D2investmentvaluationslice[0,1]
print(D2investmentvaluationItemonly)
D2investmentvaluationslice2Itemonly=D2investmentvaluationslice[0,2]
print(D2investmentvaluationslice2Itemonly)
for elem in np.nditer(D2investmentvaluation):
    print(elem)
for index, elem in np.ndenumerate(D2investmentvaluation):
    print(index, elem)
D2investmentvaluation1T010000 = np.reshape(D2investmentvaluation, (1, 10000))
print(D2investmentvaluation1T010000 )
print(D2investmentvaluation1T010000.size)
print( D2investmentvaluation1T010000.ndim)
print( D2investmentvaluation1T010000.shape)
print(D2investmentvaluation1T010000.ndim)