[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

*The problem:* Something like the class size paradox appears if you survey
children and ask how many children are in their family. Families with many
children are more likely to appear in your sample, and families with no
children have no chance to be in the sample.
Use the NSFG respondent variable NUMKDHH to construct the actual distribution
for the number of children under 18 in the household.
Now compute the biased distribution we would see if we surveyed the children
and asked them how many children under 18 (including themselves)
are in their household.
Plot the actual and biased distributions, and compute their means. As a
starting place, you can use chap03ex.ipynb.

*How I solved it:* I made a PMF of the number of children in a respondent's household, copied it, and then biased it by multiplying each x value by x, renormalized the data, and then displayed both actual and biased PMF. I then computed the means of the two PMFs by iterating through list of items and adding a weighted contribution to the mean.

'''
%matplotlib inline

import chap01soln
resp = chap01soln.ReadFemResp()
import thinkstats2
kidshousehold = resp.numkdhh
pmf = thinkstats2.Pmf(kidshousehold, label = "Actual")

 #create biased PMF
new_pmf = pmf.Copy(label=label)
for x, p in pmf.Items():
    new_pmf.Mult(x, x)      
new_pmf.Normalize()

 #plot both actual and biased PMFs
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf,new_pmf])
thinkplot.Show(xlabel = 'Number of children (<18y) per household', ylabel = 'probability')

 #calculate mean of actual and biased PMFs
mean_actual = 0
for p, x in pmf.d.items():
    mean_actual += p*x 
mean_biased = 0
for p, x in biased_pmf.d.items():
    mean_biased += p*x 
print "Actual Mean: ", mean_actual 
print "Biased Mean: ", mean_biased 
'''

*The solution:*

![Acutal vs. Biased PMF](C:\ds\metis\prework\dsp\statistics\Actual_vs_Biased_PMF.png)

The actual mean of ~1.0242 is substantially less than the biased mean of ~2.404, which serves as a great example of the class size paradox since surveying the children skews the sampling to those households with more children.
