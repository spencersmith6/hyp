import matplotlib.pyplot as plt
import numpy as np


tips = [20.8, 18.7, 19.1, 20.6, 21.9, 20.4, 22.8,
        21.9, 21.2, 20.3, 21.9, 18.3, 21.0, 20.3,
        19.2, 20.2, 21.1, 22.1, 21.0, 21.7]
n = len(tips)

fig = plt.figure()
ax = fig.add_subplot(111)

bins= np.linspace(np.min(tips),np.max(tips),7)
print bins

plt.hist(tips, bins=5, normed=1)
plt.title("Histogram of tips after beer")
plt.xlabel("% Tips")
plt.ylabel("Frequency")
plt.text(.1,.8,'mean(tips)= %f' % np.mean(tips), transform= ax.transAxes)
plt.show()


