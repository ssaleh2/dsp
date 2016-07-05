[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

*The problem:* In the BRFSS (see Section 5.4), the distribution of heights is
roughly normal with parameters m = 178 cm and s = 7.7 cm for men,
and m = 163 cm and s = 7.3 cm for women.
In order to join Blue Man Group, you have to be male between 5’10” and
6’1” (see http://bluemancasting.com). What percentage of the U.S. male
population is in this range? Hint: use scipy.stats.norm.cdf.

*How I solved it:* I used scipy.stats to use a normal cdf for height of men in centimeters and then I subtracted the different between two percentiles in that distribution. 

'''
%matplotlib inline

import scipy.stats

mean = 178
stdev = 7.7

#calculate percentiles for 5'10" and 6'1"
lower = scipy.stats.norm.cdf(70*2.54, loc=mean, scale=stdev)
upper = scipy.stats.norm.cdf(73*2.54, loc=mean, scale=stdev)

eligible = (upper - lower)*100
'''

*The solution:*

34.27% of men are able to join the Blue Man Group based on height. 