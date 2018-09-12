
import numpy as np
import scipy.fftpack
import math

############ 2 Dimensions DCT function ############
def DCT2 (mat):
    res = LINES(LINES(mat.T).T)
    return res
############ ############ ############ ############


############ Appling DCT1 for each lines ############
def LINES (mat):
    r,c = mat.shape
    res = np.zeros(mat.shape)
    for i in range(0,r):
        res[i,:] = DCT1(mat[i,:])
    return res
############ ############ ############ ############


############ 1 Dimension DCT function ############
def DCT1 (mat):
    d = mat.size
    res = np.zeros(d)

    for s in range(0,d):
        if (s == 0):
            A = 1.0/math.sqrt(d)
        else:
            A = math.sqrt(2.0/d);

        for t in range(0,d):
            res[s] = res[s] + (mat[t] * math.cos(math.pi * s * ((2.0*t+1.0)/(2.0*d))))

        res[s] = res[s] * A
    return res

############ ############ ############ ############


############ 2 Dimensions DCT function (scipy) ############
def dct2_library(my_matrix):
    dct2_matrix = scipy.fftpack.dct(scipy.fftpack.dct(my_matrix.T, norm = 'ortho').T, norm = 'ortho')
    return dct2_matrix
############ ############ ############ ############
