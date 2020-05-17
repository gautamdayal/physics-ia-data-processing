import matplotlib.pyplot as plt
import pylab as plt

Angles = [10, 20, 30, 40, 50, 60, 70]
Lift = [0.33, 0.39, 0.42, 0.38, 0.25, 0.20, 0.13]
lift_error = [0.07, 0.07, 0.06, 0.05, 0.04, 0.06, 0.04]
X = [i for i in range(71)]
Y = plt.polyval(plt.polyfit(Angles, Lift, 2), X)
newY = [Lift[i]/Angles[i] for i in range(len(Lift))]
Yforfit = plt.polyval(plt.polyfit(Angles, newY, 1), Angles)

print(newY, lift_error)


plt.style.use('seaborn')
plt.rcParams.update({'lines.markeredgewidth': 1})
plt.errorbar(Angles, newY, yerr=lift_error, ls='none', barsabove=True)
plt.plot(Angles, Yforfit)
# plt.plot([10, 70],[0.26, 0.17], '--')
# plt.plot([10, 70],[0.4, 0.09], '--')
plt.xlabel("Angle of Attack / º")
plt.ylabel("Lift Force / N")
plt.scatter(Angles,newY, color='red')
plt.show()
