import numpy as np
import matplotlib.pyplot as plt
# outfile = open('avgdata.csv', 'w')

w = 10
h = 10
d = 70
plt.figure(figsize=(w, h), dpi=d)
data = np.genfromtxt(
    "csvdata.csv", names=True,
    dtype="float", delimiter=",")

def plotEverything():
    colours = ['skyblue', 'plum', 'yellowgreen', 'lightcoral', 'teal', 'orange', 'lightseagreen', 'hotpink']
    i, j = 0, 15
    while j <= 120:
        # change to markerfacecolor[colours[i//15]] if want different colours
        plt.plot(data["Angle"][i:j], data["Neg_Mass"][i:j], 'o', markerfacecolor='orange', markeredgecolor='black')
        i += 15
        j += 15
    plt.title('Plot of My Raw Data')
    plt.xlabel('Angle of Attack/°')
    plt.ylabel('Mass Shown on Balance/-g')
    plt.show()

plotEverything()

def mean(L):
    return sum(L) / len(L)
#
# angles = [point[0] for point in data]
# n_masses = [point[1] for point in data]
#
# i, j = 0, 15
# angles_ordered = []
# n_masses_ordered = []
#
# while j <= 120:
#     angles_ordered.append(angles[i:j])
#     n_masses_ordered.append(n_masses[i:j])
#     i += 15
#     j += 15
#
# for i in range(len(angles_ordered)):
#     angles_ordered[i] = int(mean(angles_ordered[i]))
#     n_masses_ordered[i] = round(mean(n_masses_ordered[i]), 1)
    # outfile.write(str(angles_ordered[i])+','+str(n_masses_ordered[i]))
    # outfile.write('\n')

# plt.plot(angles_ordered, n_masses_ordered, 'o')
# plt.title('Plot of Averaged Data')
# plt.xlabel('Angle of Attack/°')
# plt.ylabel('Mass Shown on Balance/-g')
# plt.show()

# outfile.close()
