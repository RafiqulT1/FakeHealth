import kohta_2_foll_counts as fol
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

trusted_followers = fol.trusted_followers
untrusted_followers = fol.untrusted_followers
trusted_followees = fol.trusted_followees
untrusted_followees = fol.untrusted_followees

# 3.1. FOLLOWER DISTRIBUTIONS
# Trusted  follower histogram
hist_trusted_followers = plt.hist(trusted_followers, color='lightblue', ec='black', bins=20, range=(1, 5000), label="followers of trusted")
plt.xlabel("follower count")
plt.ylabel("number of users")
plt.title("Follower count distribution of trusted news")
plt.legend()
plt.show()


# Untrusted  follower histogram
hist_untrusted_followers = plt.hist(untrusted_followers, color='orange', ec='black', bins=20, range=(1, 5000), label="followers of untrusted")
plt.xlabel("follower count")
plt.ylabel("number of users")
plt.title("Follower count distribution of untrusted news")
plt.legend()
plt.show()

# Distribution curve of trusted followers
plt.plot(hist_trusted_followers[1][:-1], hist_trusted_followers[0], color="lightblue", label="followers of trusted")
# Distribution curve of untrusted followers
plt.plot(hist_untrusted_followers[1][:-1], hist_untrusted_followers[0], color="orange", label="followers of untrusted")

plt.xlabel("follower count")
plt.title("Follower count distributions")
plt.legend()
plt.show()
print(hist_trusted_followers[0])
print(hist_untrusted_followers[0])


# formula for scaling between 0 - 1: x_norm = (x-np.min(x))/(np.max(x)-np.min(x))
scaled_trusted = (hist_trusted_followers[0] - np.min(hist_trusted_followers[0])) / (np.max(hist_trusted_followers[0])-np.min(hist_trusted_followers[0]))
scaled_untrusted = (hist_untrusted_followers[0] - np.min(hist_untrusted_followers[0])) / (np.max(hist_untrusted_followers[0])-np.min(hist_untrusted_followers[0]))

# Scaled distribution curve of trusted followers
plt.plot(hist_trusted_followers[1][:-1], scaled_trusted, color="lightblue", label="followers of trusted")
# Scaled distribution curve of untrusted followers
plt.plot(hist_untrusted_followers[1][:-1], scaled_untrusted, color="orange", label="followers of untrusted")
plt.xlabel("follower count")
plt.title("Follower count distributions")
plt.legend()
plt.show()


# 3.2. FOLLOWEE DISTRIBUTIONS

# Trusted  followee histogram
hist_trusted_followees = plt.hist(trusted_followees, color='lightblue', ec='black', bins=20, range=(1, 5000), label="followees of trusted")
plt.xlabel("followee count")
plt.ylabel("number of users")
plt.title("Followee count distribution of trusted news")
plt.legend()
plt.show()


# Untrusted  followee histogram
hist_untrusted_followees = plt.hist(untrusted_followees, color='orange', ec='black', bins=20, range=(1, 5000), label="followees of untrusted")
plt.xlabel("followee count")
plt.ylabel("number of users")
plt.title("Follower count distribution of untrusted news")
plt.legend()
plt.show()

# Distribution curve of trusted followees
plt.plot(hist_trusted_followers[1][:-1], hist_trusted_followees[0], color="lightblue", label="followees of trusted")
# Distribution curve of untrusted followees
plt.plot(hist_untrusted_followees[1][:-1], hist_untrusted_followees[0], color="orange", label="followees of untrusted")

plt.xlabel("followee count")
plt.title("Followee count distributions")
plt.legend()
plt.show()
print(hist_trusted_followees[0])
print(hist_untrusted_followees[0])


# formula for scaling between 0 - 1: x_norm = (x-np.min(x))/(np.max(x)-np.min(x))
scaled_trusted = (hist_trusted_followees[0] - np.min(hist_trusted_followees[0])) / (np.max(hist_trusted_followees[0])-np.min(hist_trusted_followees[0]))
scaled_untrusted = (hist_untrusted_followees[0] - np.min(hist_untrusted_followees[0])) / (np.max(hist_untrusted_followees[0])-np.min(hist_untrusted_followees[0]))

# Scaled distribution curve of trusted followees
plt.plot(hist_trusted_followees[1][:-1], scaled_trusted, color="lightblue", label="followees of trusted")
# Scaled distribution curve of untrusted followees
plt.plot(hist_untrusted_followees[1][:-1], scaled_untrusted, color="orange", label="followees of untrusted")
plt.xlabel("followee count")
plt.title("Followee count distributions")
plt.legend()
plt.show()



# # # -----------------------------
# Kohta 4
# # power law distribution made with https://www.youtube.com/watch?v=yjeMEuK6hik&t=4s&ab_channel=PhysicsWithNero

# 4.1. TRUSTED FOLLOWER
# Fitting a power law distribution to trusted follower distribution
plt.loglog(hist_trusted_followers[1][:-1], hist_trusted_followers[0], "r.")

plt.grid()
plt.show()
plt.clf()

ln_hist_x = np.log(hist_trusted_followers[1])
ln_hist_y  = np.log(hist_trusted_followers[0])

b, ln_a = np.polyfit(ln_hist_x[:-1], ln_hist_y, 1)
a = np.exp(ln_a)

# power law: y = b * x ** a
print(f"power = {b:.2f}, sigma = {a:.2f}")

plt.plot(hist_trusted_followers[1][:-1],hist_trusted_followers[0], "r.", label="points from the follower distribution")
plt.plot(hist_trusted_followers[1][:-1], a*hist_trusted_followers[1][:-1]**b, "k-", label="power law distribution")
plt.legend()
plt.title("Fitting power law distribution to follower count distribution of trusted news")
plt.grid()
plt.show()
plt.clf()

plt.loglog(hist_trusted_followers[1][:-1],hist_trusted_followers[0], "r.", label="points from the follower distribution")
plt.loglog(hist_trusted_followers[1][:-1], a*hist_trusted_followers[1][:-1]**b, "k-", label="power law distribution")
plt.legend()
plt.title("Fitting power law distribution to follower count distribution of trusted news")
plt.grid()
plt.show()
plt.clf()


# 4.2. UNTRUSTED FOLLOWER
# Fitting a power law distribution to untrusted follower distribution
plt.loglog(hist_untrusted_followers[1][:-1], hist_untrusted_followers[0], "r.")

plt.grid()
plt.show()
plt.clf()

ln_hist_x = np.log(hist_untrusted_followers[1])
ln_hist_y  = np.log(hist_untrusted_followers[0])

b, ln_a = np.polyfit(ln_hist_x[:-1], ln_hist_y, 1)
a = np.exp(ln_a)

print(f"power = {b:.2f}, sigma = {a:.2f}")

plt.plot(hist_trusted_followers[1][:-1],hist_trusted_followers[0], "r.", label="points from the follower distribution")
plt.plot(hist_trusted_followers[1][:-1], a*hist_trusted_followers[1][:-1]**b, "k-", label="power law distribution")
plt.legend()
plt.title("Fitting power law distribution to follower count distribution of untrusted news")
plt.grid()
plt.show()
plt.clf()

plt.loglog(hist_trusted_followers[1][:-1],hist_trusted_followers[0], "r.", label="points from the follower distribution")
plt.loglog(hist_trusted_followers[1][:-1], a*hist_trusted_followers[1][:-1]**b, "k-", label="power law distribution")
plt.legend()
plt.title("Fitting power law distribution to follower count distribution of untrusted news")
plt.grid()
plt.show()
plt.clf()


# 4.3. TRUSTED FOLLOWEE

# Fitting a power law distribution to trusted followee distribution
plt.loglog(hist_trusted_followers[1][:-1], hist_trusted_followees[0], "r.")

plt.grid()
plt.show()
plt.clf()

ln_hist_x = np.log(hist_trusted_followees[1])
ln_hist_y  = np.log(hist_trusted_followees[0])

b, ln_a = np.polyfit(ln_hist_x[:-1], ln_hist_y, 1)
a = np.exp(ln_a)

print(f"power = {b:.2f}, sigma = {a:.2f}")

plt.plot(hist_trusted_followees[1][:-1],hist_trusted_followees[0], "r.", label="points from the followee distribution")
plt.plot(hist_trusted_followees[1][:-1], a*hist_trusted_followees[1][:-1]**b, "k-", label="power law distribution")
plt.legend()
plt.title("Fitting power law distribution to followee count distribution of trusted news")
plt.grid()
plt.show()
plt.clf()

plt.loglog(hist_trusted_followees[1][:-1],hist_trusted_followees[0], "r.", label="points from the followee distribution")
plt.loglog(hist_trusted_followees[1][:-1], a*hist_trusted_followees[1][:-1]**b, "k-", label="power law distribution")
plt.legend()
plt.title("Fitting power law distribution to followee count distribution of trusted news")
plt.grid()
plt.show()
plt.clf()

# 4.4. UNTRUSTED FOLLOWEE

# Fitting a power law distribution to untrusted follower distribution
plt.loglog(hist_untrusted_followees[1][:-1], hist_untrusted_followees[0], "r.")

plt.grid()
plt.show()
plt.clf()

ln_hist_x = np.log(hist_untrusted_followees[1])
ln_hist_y  = np.log(hist_untrusted_followees[0])

b, ln_a = np.polyfit(ln_hist_x[:-1], ln_hist_y, 1)
a = np.exp(ln_a)

print(f"power = {b:.2f}, sigma = {a:.2f}")

plt.plot(hist_trusted_followees[1][:-1],hist_trusted_followees[0], "r.", label="points from the followee distribution")
plt.plot(hist_trusted_followees[1][:-1], a*hist_trusted_followees[1][:-1]**b, "k-", label="power law distribution")
plt.legend()
plt.title("Fitting power law distribution to followee count distribution of untrusted news")
plt.grid()
plt.show()
plt.clf()

plt.loglog(hist_trusted_followees[1][:-1],hist_trusted_followees[0], "r.", label="points from the followee distribution")
plt.loglog(hist_trusted_followees[1][:-1], a*hist_trusted_followees[1][:-1]**b, "k-", label="power law distribution")
plt.legend()
plt.title("Fitting power law distribution to followee count distribution of untrusted news")
plt.grid()
plt.show()
plt.clf()