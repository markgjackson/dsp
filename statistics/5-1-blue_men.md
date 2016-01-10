[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Thus 34.2746837631% of the male population could be a Blue Man.

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

mu = 178
sigma = 7.7

lowerHeight=177.8 #70 inches
upperHeight=185.42 #73 inches

upperCdf = scipy.stats.norm.cdf(upperHeight,mu,sigma)
lowerCdf = scipy.stats.norm.cdf(lowerHeight,mu,sigma)

diffCdf = upperCdf-lowerCdf
perc = diffCdf * 100

print "The upper cdf is " + str(upperCdf)
print "The lower cdf is " + str(lowerCdf)

print "Thus " + str(perc) + "% of the male population could be a Blue Man."

print "All done"

