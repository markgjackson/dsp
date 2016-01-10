[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

The Pearson Correlation between birth weight and mother's age is 0.0688339703541
The Spearman Correlation between birth weight and mother's age is 0.0946100410966
Weak correlation

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

print "Loading data..."
preg = nsfg.ReadFemPreg()
print "Figuring out live births"
live = preg[preg.outcome == 1]
live = live.dropna(subset =['totalwgt_lb','agepreg'])

birthWeight = live.totalwgt_lb
mothersAge = live.agepreg

#print birthWeight
#print mothersAge

thinkplot.Scatter(mothersAge,birthWeight,alpha=0.2)
thinkplot.Show(ylabel="Birth Weight (lbs)",xlabel="Mother's Age (years)")

bins = np.arange(5,50,5)
indices = np.digitize(mothersAge,bins)
groups = live.groupby(indices)

mothersAgeBinned = [group.agepreg.mean() for i,group in groups]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]

for percent in [75,50,25]:
    weights = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' % percent
    thinkplot.Plot(mothersAgeBinned, weights, label = label)

thinkplot.Show(ylabel="Birth Weight (lbs)",xlabel="Mother's Age (years)")

def Cov(xs, ys, meanx = None, meany = None):
    xs = np.asarray(xs)
    ys = np.asarray(ys)

    if meanx is None:
        meanx = np.mean(xs)
    if meany is None:
        meany = np.mean(ys)

    cov = np.dot(xs-meanx, ys-meany) / len(xs)
    return cov

def Corr(xs,ys):
    xs = np.asarray(xs)
    ys = np.asarray(ys)

    meanx = np.mean(xs)
    varx = np.var(xs)
    meany = np.mean(ys)
    vary = np.var(ys)

    corr = Cov(xs, ys, meanx, meany) / math.sqrt(varx * vary)
    return corr

print "The Pearson Correlation between birth weight and mother's age is " + str(Corr(birthWeight,mothersAge))


def SpearmanCorr(xs,ys):
    xranks = pandas.Series(xs)
    yranks = pandas.Series(ys)
    return xs.corr(ys,method='spearman')

print "The Spearman Correlation between birth weight and mother's age is " + str(SpearmanCorr(birthWeight,mothersAge))


print "All done"
