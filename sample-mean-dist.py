import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

tips = [20.8, 18.7, 19.1, 20.6, 21.9, 20.4, 22.8,
        21.9, 21.2, 20.3, 21.9, 18.3, 21.0, 20.3,
        19.2, 20.2, 21.1, 22.1, 21.0, 21.7]
n = len(tips)
sMean = np.mean(tips)
sSd = np.std(tips, ddof=1)

pMean = 20
pSd = sSd/np.sqrt(n)

print sMean
plt.axis([pMean-4*pSd, pMean+4*pSd, 0, stats.norm.pdf(pMean,pMean,pSd)+.1])
x = np.arange(pMean-10, pMean+10, .001)
y = stats.norm.pdf(x,pMean,pSd)
plt.plot(x, y, color='red')
plt.text(sMean, .2, "Sample Mean= %1.2f" %sMean)
plt.plot(sMean,0,"D")
plt.show()