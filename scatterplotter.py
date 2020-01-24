import numpy as np
import matplotlib.pyplot as plt

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
        plt.plot(data["Angle"][i:j], data["Neg_Mass"][i:j], 'o', markerfacecolor='black', markeredgecolor='black')
        i += 15
        j += 15
    plt.title('Plot of My Raw Data')
    plt.xlabel('Angle of Attack/°')
    plt.ylabel('Mass Shown on Balance/-g')
    plt.show()

plotEverything()
