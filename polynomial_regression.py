import numpy
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# Make polynomial model
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# Concifugre line display (start at position 1 and end in 22)
myline = numpy.linspace(1, 22, 100)

# Display 
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()