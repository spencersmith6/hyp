import numpy as np

tips = [20.8, 18.7, 19.1, 20.6, 21.9, 20.4, 22.8,
        21.9, 21.2, 20.3, 21.9, 18.3, 21.0, 20.3,
        19.2, 20.2, 21.1, 22.1, 21.0, 21.7]

n = len(tips)
TRIALS = 5000
mean = 20
sd = np.std(tips, ddof=1)

X_bar= []
for x in range(TRIALS):
    sample = np.random.normal(mean, sd, len(tips))
    X = np.mean(sample)
    X_bar.append(X)

greater = sum([X_bar[x] >= np.mean(tips) for x in range(len(X_bar))])

p = 2*(greater/float(TRIALS))

print "observed mean = " + str(np.mean(tips))
print "num greater than mean(tips) = " + str(greater)
print "p-value from bootstrapping (ratio of X_ >= mean(tips)) is " + str(p)