'''
from scipy.special import factorial

n=5
result=factorial(n,exact=True) #Exact is used to eliminate the decimal op
print("Factorial of",n,"is",result)
'''
'''
from scipy.stats import norm

mean=0
std_dev=1
x=1.5

pdf_value = norm.pdf(x,mean, std_dev)
cdf_value = norm.cdf(x,mean, std_dev)
#CDF will always be less than PDF
print("Porbablity Density Function at x:", pdf_value)
print("Cumulative Distribution Function at X:",cdf_value)
'''

'''
from scipy.optimize import minimize

def func(x):
    return x**2 + 5*x +10

result= minimize(func,x0=0)
print("Min value:",result.fun)
print("Minimizer:",result.x)
'''
'''
import numpy as np
from scipy.interpolate import interp1d

x = np.array([0,1,2,3,4])
y = np.array([0,1,4,9,16])

interp_func = interp1d(x,y,kind='cubic')
new_x=2.5
interp_value = interp_func(new_x)
print("Interpolated value at x = ",new_x,"is",interp_value)
'''
'''
import  numpy as np
from scipy import integrate
#function to be intergrated
def func(x):
    return np.sin(x)

#perform numerical using scipy's intergrate.quad()
result, error= integrate.quad(func, 0 ,np.pi)

print("Numerical intergration result:")
print("Intergrate value:",result)
print("Estimated error:", error)
'''

import numpy as np
from scipy import stats,optimize,interpolate

#generating sample data
x = np.linspace(0,10,20)
y = np.sin(x)+ np.random.normal(0,0.1,20)

print(x)
print(y)

def func(x,a,b):
    return a* np.sin(b*x)
params, params_covariance = optimize.curve_fit(func,x,y)
print("Curve Fitting Parameter:")
print("Amplitude(a):",params[0])
print("Frequency(B):",params[1])

data= np.random.randint(108)
mean= np.mean(data)
median= np.median(data)
std_dev= np.std(data)
skewness= stats.skew(data)
kurtosis= stats.kurtosis(data)

print("Stastical OPerations:")
print("Mean:",mean)
print("median:",median)
print("Standard Deviation:",std_dev)
print("Skewness:",skewness)
print("Kurtosis:",kurtosis)
