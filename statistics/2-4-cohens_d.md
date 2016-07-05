[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

*The problem*: Using the variable totalwgt_lb, investigate whether first babies
are lighter or heavier than others. Compute Cohen’s d to quantify the
difference between the groups. How does it compare to the difference in
pregnancy length?

*How I solved it*: I took the difference of the means of the first and other babies and then determining which mean was larger. I then combined the variance of the first and others to ultimately calculate Cohen's d.

'''
def CohensWeightDiff(firsts, others):
    mean_firsts = firsts.totalwgt_lb.mean()
    mean_others = others.totalwgt_lb.mean()
#determining which is lighter/heavier
    diff_mean = abs(mean_firsts - mean_others)
    if mean_firsts > mean_others:    
        print("firsts babies [%f] are HEAVIER than other babies[%f]." %(mean_firsts, mean_others))
    else:
        print("firsts babies [%f] are LIGHTER than other babies[%f]." %(mean_firsts, mean_others))
    var_firsts = firsts.totalwgt_lb.var()
    var_others = others.totalwgt_lb.var()
    combined_var = (len(firsts)*var_firsts + len(others)*var_others)/(len(firsts) + len(others))
    final = diff_mean / math.sqrt(combined_var)
    return final     
  '''

*The solution:* The Cohen's d for weight is ~0.089, while for pregnancy length it was ~0.029. Both do not have a large difference between groups.