import numpy as np
import scipy.misc as scm
import cv2
a=np.array([[[1,2,3],	[4,5,6],   [7,8,9]],
	    [[10,11,12],[13,14,15],[16,17,18]],
	    [[19,20,21],[22,23,24],[25,26,27]]])
cv2.imwrite("filename.png",a)
dutu=cv2.imread('filename.png')
print dutu
lingwai=scm.imread('filename.png').astype(np.float32)
print("diege********")
print lingwai
#
'''[[[ 3.  2.  1.]
  [ 6.  5.  4.]
  [ 9.  8.  7.]]

 [[12. 11. 10.]
  [15. 14. 13.]
  [18. 17. 16.]]

 [[21. 20. 19.]
  [24. 23. 22.]
  [27. 26. 25.]]]
'''

