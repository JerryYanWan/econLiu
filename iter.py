import numpy as np


# initialize all the parameters
w = 1.
lambda_H = 1.0
lambda_L = 1.0
mu = 1.0
alpha = 1.0
p = 0.5
s = 0.1
beta = lambda_H + lambda_L + mu + alpha

T = 5
I = 5
N = 5

V_test = np.zeros((T, I, N))


# normal recursive function
def V(t, i, n):
    if (t == 0):
        return 0
    elif (n == 0 and i != 0):
        return w * i + (lambda_H + lambda_L) / beta * V(t - 1, i + 1, 0) + \
          mu / beta * V(t-1, i-1, 0) + \
          alpha / beta * V(t-1, i, 0)
    elif (n != 0 and i == 0):
        return (lambda_H + lambda_L) / beta * np.min([V(t-1, 1, n), p*(V(t-1, 0, n-1)+s)+(1-p)*V(t-1, 1, n)]) + \
          mu / beta * V(t-1, 0, n) + \
          alpha / beta * V(t-1, 0, n)
    else:
        return w * i + (lambda_H + lambda_L) / beta * np.min([V(t-1, i+1, n), p*(V(t-1, i, n-1)+s)+(1-p)*V(t-1, i+1, n)]) + \
          mu / beta * V(t-1, i-1, n) + \
          alpha / beta * V(t-1, i, n)

def get(t, i, n):
    if (t >= T or n >= N or i >= I or t < 0 or n < 0 or i < 0):
        return 0.
    else:
        return V_test[t, i, n]

# fast version using dynamic programming
def V_fast(t, i, n):
    if (t <= 0):
        return 0.
    elif (n == 0 and i != 0):
        return w * i + (lambda_H + lambda_L) / beta * get(t - 1, i + 1, 0) + \
          mu / beta * get(t-1, i-1, 0) + \
          alpha / beta * get(t-1, i, 0)
    elif (n != 0 and i == 0):
        return (lambda_H + lambda_L) / beta * np.min([get(t-1, 1, n), p*(get(t-1, 0, n-1)+s)+(1-p)*get(t-1, 1, n)]) + \
          mu / beta * get(t-1, 0, n) + \
          alpha / beta * get(t-1, 0, n)
    else:
        return w * i + (lambda_H + lambda_L) / beta * \
          np.min([get(t-1, i+1, n), p*(get(t-1, i, n-1)+s)+(1-p)*get(t-1, i+1, n)]) + \
          mu / beta * get(t-1, i-1, n) + \
          alpha / beta * get(t-1, i, n)

for t in xrange(0, T):
    for i in xrange(0, I):
        for n in xrange(0, N):
            V_test[t, i, n] = V(t, i, n)

print V_test
