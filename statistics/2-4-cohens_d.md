[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Cohen's d for this is -0.0886729270726, which is quite small and thus I would say not significant.

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
import thinkstats2

def CohenEffectSize(group1,group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1,n2 = len(group1),len(group2)

    pooled_var = (n1*var1 + n2*var2)/(n1+n2)
    d = diff / math.sqrt(pooled_var)
    return d


print "Loading data..."
preg = nsfg.ReadFemPreg()
print "Figuring out live births"
live = preg[preg.outcome == 1]
print "Figuring out first-born births"
firsts = live[preg.birthord == 1]
print "Figuring out non-first born births"
others = live[preg.birthord != 1]
firstWeights = firsts.totalwgt_lb
otherWeights = others.totalwgt_lb

#print "The first few first-born weights are " + str(firstWeights)

print "Cohen's d for this is " + str(CohenEffectSize(firstWeights,otherWeights))

width=0.45
thinkplot.PrePlot(2)
histFirst = thinkstats2.Hist(firstWeights,label='First-born Birthweights')
thinkplot.Hist(histFirst)
histOther = thinkstats2.Hist(otherWeights,label='Non-first-born Birthweights')
thinkplot.Hist(histOther)
thinkplot.Show(xlabel='pounds',ylabel='frequency')

print "all done"


