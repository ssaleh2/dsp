# Matrix Algebra
"""
You should be familiar with the following concepts:
* adding vectors
* matrix multiplication
* matrix inverse
* how to visualize lines and planes and hyperplanes; dot product
* systems of linear equations
* eigenvalues

### Exercises  

There are matrix operations exercises in the [Matrix Algebra Worksheet](math/matrix_algebra_worksheet.pdf).  Print out the worksheet and complete the computations by hand.  You can check your work in Python.

---

Place your Python code (with results in comment) in this file: [matrix_algebra.py](math/matrix_algebra.py)
"""

import numpy as np

A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1,-1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.matrix([[1],[8],[0],[5]])

#1.1) 2x3
print A.shape
#1.2) 2x2
print B.shape
#1.3) 3x2
print C.shape
#1.4) 2x3
print D.shape
#1.5) 1x4
print u.shape
#1.6) 4x1
print w.shape

#2.1) [ 9  7 -4  9]
print u+v
#2.2) [ 3 -3 -2  1]
print u-v
#2.3) [ 36  12 -18  30]
print 6*u
#2.4) [18 10  3 20]
print u*v
#2.5) 8.602
print np.linalg.norm(u)

#3.1) Undefined
print "3.1) ",
try:
    print np.add(A,C)
except:
    print("Undefined")
#3.2) 
# [[-4 -7 -3]
# [ 3  6  4]]
print "3.2) ",
try:
    print np.subtract(A, np.transpose(C))
except:
    print("Undefined")
#3.3)
#[[14  3  3]
# [ 2  7  9]]
print "3.3) ",
try:
    print np.add(np.transpose(C), 3*D)
except:
    print("Undefined")
#3.4) 
#[[-1 -5 -1]
# [ 2  7  4]]
print "3.4) ",
try:
    print np.dot(B,A)
except:
    print("Undefined")
#3.5) Undefined
print "3.5) ",
try:
    print np.dot(B,np.transpose(A))
except:
    print("Undefined")
#3.6) Undefined
print "3.6) ",
try:
    print np.dot(B,C)
except:
    print("Undefined")
#3.7) 
#[[ 5 -6]
# [ 9 -8]
# [ 6 -6]]
print "3.7) ",
try:
    print np.dot(C,B)
except:
    print("Undefined")
#3.8) 
# [[1 -4]
#  [0 1]]
print "3.8) ",
try:
    print np.linalg.matrix_power(B,4)
except:
    print("Undefined")
#3.9) 
# [[14 28]
# [28 69]]
print "3.9) ",
try:
    print np.dot(A,np.transpose(A))
except:
    print("Undefined")
#3.10) 
#[[10 -4  0]
# [-4  8  8]
# [ 0  8 10]]
print "3.10) ",
try:
    print np.dot(np.transpose(D),D)
except:
    print("Undefined")
