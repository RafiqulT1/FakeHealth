import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#--MAKE TEST DATA--#
#make this example reproducible.
np.random.seed(1)
#create numpy array with 1000 values that follow normal dist with mean=10 and sd=2
data = np.random.normal(size=1000, loc=10, scale=2)
data2 = np.random.normal(size=900, loc=7, scale=2)
#----#


def distribution_curve(data, max_value=20, label=None):
    '''
    Draw and plot distribution curve of data.
    '''
    density = stats.kde.gaussian_kde(data)
    x = np.arange(0., max_value, .1)
    plt.plot(x, density(x), label=label)


# Create histograms
#plt.hist(data, color='lightgreen', ec='black', bins=15, label="data")
#plt.hist(data2, color='lightblue', ec='black', bins=15, label="data2")

# Make distribution curve 1
distribution_curve(data, label="data")
# Make distribution curve 2
distribution_curve(data2, label="data2")


plt.legend() # add labels
plt.show()