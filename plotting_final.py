import matplotlib.pyplot as plt
import pylab as plt

Angles = [0, 10, 20, 30, 40, 50, 60, 70]
Lift = [0.24, 0.33, 0.39, 0.42, 0.38, 0.25, 0.20, 0.13]
lift_error = [0.04, 0.07, 0.07, 0.06, 0.05, 0.04, 0.06, 0.04]

plt.style.use('seaborn')
plt.rcParams.update({'lines.markeredgewidth': 1})
plt.errorbar(Angles, Lift, yerr=lift_error, ls='none', barsabove=True)
X = [i for i in range(71)]
Y = plt.polyval(plt.polyfit(Angles, Lift, 2), X)
plt.plot(X, Y)
plt.xlabel("Angle of Attack / º")
plt.ylabel("Lift Force / N")
plt.scatter(Angles,Lift, color='red')
plt.show()
