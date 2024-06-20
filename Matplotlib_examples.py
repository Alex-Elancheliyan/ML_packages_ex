import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,6,8,10]


#LINE CHART
#shows the connectivity b/w data
plt.plot(x,y,marker='o')

#Adding labels names to the plotting

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Line Plot')

#Scattered chart
#shows distribution of data


plt.scatter(x,y,marker='o',color='red')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('scatter plot')
plt.show()


# Bar Chart

plt.bar(x,y,color='yellow') #bar chart cant have Marker  attribute
categories=['A','B','C','D','E']
values=[25,30,15,20,10]
plt.bar(categories,values,color='yellow')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('BAR CHART')
plt.show()


categories=['A','B','C','D','E']
values=[25,30,15,20,10]
plt.bar(categories,values,color='yellow')


#Histograms-A histogram is a graph that shows the frequency of numerical data using rectangles.
#The height of a rectangle (the vertical axis) represents the distribution frequency of a variable
#(the amount, or how often that variable appears).

data=[1,2,2,3,3,4,4,4,4,5,5,5,5,6,6]
plt.hist(data, bins=5, edgecolor='red',color='yellow') #bins represented no of bars #edgecolor is colour of edges
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Histogram')


#PIE chart
#pie chart cannot deal with string data
#pie chart is used in percentage distribution

values=[250,300,150,200,100]
categories=['A','B','C','D','E']
explodedata=(0,0.1,0,0,0)
col=['red','yellow','blue','pink','green']
plt.title('PIE CHART')
plt.pie(values,labels=categories,shadow=True,explode=explodedata,autopct='%1.0f%%',colors=col) #autopct is auto percentage


#SIN function
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 5)
y = np.sin(x)

# Create a line plot
plt.plot(x, y, label='sin(x)', color='yellow',linewidth=2,marker='o')

# Add labels and title
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Function')

# Add grid lines
plt.grid(True)
# Add legend
plt.legend()
# Show the plot
plt.show()


import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 100)
print(data)

# Create a histogram
plt.hist(data, bins=10, edgecolor='black', color='skyblue')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram with Custom Data')

# Show the plot
plt.show()


#LINE Chart
import numpy as np
import matplotlib.pyplot as plt

# Sample data for the x-axis and two y-axis variables
# Replace these arrays with your own datasets
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a line plot with two data series
plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='red')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with Custom Data')

# Add legend to identify data series
plt.legend()

# Show the plot
plt.grid(True)
plt.show()


#LINE WITH MULTIPLE SERIES
import matplotlib.pyplot as plt

# Sample data for three data series
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [3, 6, 2, 5, 8]

# Create a line plot with multiple data series
plt.plot(x, y1, label='Series 1', marker='o')
plt.plot(x, y2, label='Series 2', marker='s')
plt.plot(x, y3, label='Series 3', marker='^')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with Multiple Data Series')

# Add legend to identify data series
plt.legend()

# Show the plot
plt.show()





plt.show()
