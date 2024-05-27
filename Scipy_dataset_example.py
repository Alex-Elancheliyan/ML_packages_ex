import numpy as np
from scipy import stats
data= np.array([10,15,12,18,20,25,14,22,14,22,16,19])

mean_value=np.mean(data)
std_deviation=np.std(data)

print(mean_value)

print(std_deviation)

x= np.array([1,2,3,4,5])
y= np.array([2,4,5,8,6])

slope,intercept, r_value, p_value, std_err= stats.linregress(x,y)

print(slope)
print(intercept)
print(r_value)
print(p_value)

print('''----------------------------------------''')

#PERFORMING T TEST
group1= np.array([23,25,18,27,21])
group2= np.array([30,29,31,28,27])
t_statistics, p_value = stats.ttest_ind(x,y)

print (t_statistics)
print(p_value)
