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
        plt.plot(data["Angle"][i:j], data["Neg_Mass"][i:j], 'o', markerfacecolor=colours[i//15], markeredgecolor='black')
        i += 15
        j += 15
    plt.title('Plot of My Raw Data')
    plt.xlabel('Angle of Attack/°')
    plt.ylabel('Mass Shown on Balance/-g')
    plt.show()

# plotEverything()

# outfile.close()

def mean(L):
    return sum(L) / len(L)

angles = [point[0] for point in data]
n_masses = [point[1] for point in data]

print(angles)
