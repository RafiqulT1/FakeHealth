# power law distribution made with https://www.youtube.com/watch?v=yjeMEuK6hik&t=4s&ab_channel=PhysicsWithNero
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
    density = stats.gaussian_kde(data)
    x = np.arange(0., max_value, .1)
    plt.plot(x, density(x), label=label)

# Create histograms
hist1 = plt.hist(data, color='lightgreen', ec='black', bins=10, label="data")
#plt.hist(data2, color='lightblue', ec='black', bins=15, label="data2")

# Make distribution curve 1
#distribution_curve(data, label="data")
# Make distribution curve 2
#distribution_curve(data2, label="data2")

hist1_x = hist1[1]
hist1_y = hist1[0]
print(hist1_x)
print(hist1_y)

plt.legend() # add labels
plt.show()
plt.clf()


plt.plot(hist1_x[:-1], hist1_y, "r.")

plt.show()
plt.clf()

plt.loglog(hist1_x[:-1], hist1_y, "r.")

plt.grid()
plt.show()
plt.clf()

ln_hist1_x = np.log(hist1_x)
ln_hist1_y  = np.log(hist1_y)



b, ln_a = np.polyfit(ln_hist1_x[:-1], ln_hist1_y, 1)
a = np.exp(ln_a)
#print(ln_hist1_x[:-1], ln_hist1_y)
print(f"power = {b:.2f}, sigma = {a:.2f}")

plt.plot(hist1_x[:-1], hist1_y, "r.")
plt.plot(hist1_x[:-1], a*hist1_x[:-1]**b, "k-")

plt.grid()
plt.show()
plt.clf()