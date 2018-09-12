import time
import numpy as np
from DCTs import DCT2, dct2_library
import sys


# Initialize random matrix of arbitrary dimensions
n = int(sys.argv[1])
random_matrix = np.random.random((n, n))


####### DCT2 LIBRARY: Calculating the DCT matrix and the performance (time) ####### ####### ####
time0= time.clock()
res_matrix = dct2_library(random_matrix)
time1= time.clock()

print "Total time spent using the Scipy library:", time1-time0, "seconds"
print "\n"
####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######


####### DCT2 IMPLEMENTATION: Calculating the DCT matrix and the performance (time) ####### ####### ####
time2= time.clock()
res_matrix2 = DCT2(random_matrix)
time3= time.clock()

print "Total time spent using the full implmentation: ", time3-time2, "seconds"
print "\n"
####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######
