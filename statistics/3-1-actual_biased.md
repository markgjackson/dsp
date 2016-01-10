[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Mean number of children in unbiased data is 1.02420515504
Mean number of children in biased data is 2.40367910066

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



print "Starting"
dct_file = '2002FemResp.dct'
dat_file = '2002FemResp.dat.gz'
dct = thinkstats2.ReadStataDct(dct_file)
df = dct.ReadFixedWidth(dat_file, compression='gzip')

def childrenBiaser(children,repeater):
    biasedList = []
    index = 0
    while index < repeater:
        biasedList.append(children)
        index += 1
    return biasedList


def listBiaser(unbiased):
    biasedList=[]
    for index in range(0,len(unbiased)):
         biasedList.append(childrenBiaser(unbiased[index],unbiased[index]))
    return [item for sublist in biasedList for item in sublist]

biasedSeries = pandas.Series(listBiaser(df['numkdhh']))


#print biasedSeries


print "Preparing graph"
#print df['numkdhh'][0:5]

width=0.45
thinkplot.PrePlot(2)
histActual = thinkstats2.Hist(df['numkdhh'],label='Unbiased')
thinkplot.Hist(histActual)
histBiased = thinkstats2.Hist(biasedSeries,label='Biased')
thinkplot.Hist(histBiased)

thinkplot.Show(xlabel='Children in family',ylabel='Number of families')

meanActual = df['numkdhh'].mean()
meanBiased = biasedSeries.mean()

print "Mean number of children in unbiased data is " + str(meanActual)
print "Mean number of children in biased data is " + str(meanBiased)
print "All done"

