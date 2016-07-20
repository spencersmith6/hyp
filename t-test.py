import numpy as np
import scipy.stats as stats

tips = [20.8, 18.7, 19.1, 20.6, 21.9, 20.4, 22.8,
        21.9, 21.2, 20.3, 21.9, 18.3, 21.0, 20.3,
        19.2, 20.2, 21.1, 22.1, 21.0, 21.7]
n = len(tips)
sMean = np.mean(tips)
sSd = np.std(tips, ddof=1)

t = (sMean - 20) / (sSd / np.sqrt(n))

print  "t is " +str(t)

p = (1 - stats.t.cdf(t, n - 1))

print "one-sided p-value is " +str(p)
print "two-sided p-value is " + str(2*p)
print "p-value (from t-test) = " + str(2*p) + ", Reject H0"