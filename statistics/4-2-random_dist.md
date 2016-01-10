[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

Yes, the distribution is uniform.

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
ranLength=1000
ranList=[]
for index in range(0,ranLength):
    ranList.append(random.random())

#print ranList
#ranSeries = pandas.Series(ranList)
#print ranSeries
pmf = thinkstats2.Pmf(ranList,label="Random")
#ranHist = thinkstats2.Hist(ranSeries,label="Random")
#print pmf
wid= float(1) / float(ranLength)
thinkplot.Hist(pmf,width=wid)
thinkplot.Show(xlabel='Value',ylabel='probability')

cdf=thinkstats2.Cdf(ranList)
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='Value',ylabel='CDF')

print "All done"

