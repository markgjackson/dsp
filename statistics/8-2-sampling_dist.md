[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

('rmse L', 1.1449914934512464)
('mean error L', 0.37124505572638605)
The 90% confidence interview is (1.2344971266121401, 4.4026365684906024)

Code:

# Python program that can be executed to report whether particular
# python packages are available on the system.

#import os
import math
#import sys
import numpy as np
import scipy
import pandas
import thinkplot
import matplotlib
import nsfg
import random
import thinkstats2

print "Starting"

def MeanError(estimates, actual):
    errors = [estimate-actual for estimate in estimates]
    return np.mean(errors)

def RMSE(estimates,actual):
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)

def Estimate3(n,m):
    lam = 2

    means = []

    for _ in range(m):
        xs = np.random.exponential(1.0/lam,n)
        #print xs
        L = 1 / np.mean(xs)
        #print xs
        #print L
        means.append(L)
        
    #print means
    print "Just ran " + str(m) + " trials."
    print('rmse L', RMSE(means,lam))
    print('mean error L', MeanError(means, lam))

    cdf = thinkstats2.MakeCdfFromList(means)
    #print cdf
    thinkplot.Cdf(cdf,label="lambda = 2, 1000 runs")
    thinkplot.Show(xlabel='L',ylabel='CDF')
    ci = cdf.Percentile(5),cdf.Percentile(95)
    print "The 90% confidence interview is " + str(ci)

Estimate3(7,1000)

print "All done"
