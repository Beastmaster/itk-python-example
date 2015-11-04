
# Author: QIN Shuo
# Date:   2015/10/26
# This is a test file for itk
# This example demonstrates how to use FixedArray class 
# 
# Note:
#   FixedArray calss implement operator[] for c++ 
#   Use Set/GetElement function to access element instead in wrap languages(python for example)
#   There is no New() function in python wrap, but you should add () to initialize it

import itk

# created an fixed 3-length unsigned char array 
# Note: the () in the last is essential!
array = itk.FixedArray[itk.UC,3]()  

print ("init is ",array)

# use SetElement function to set menber instead of operator []
array.SetElement(0,1)
array.SetElement(1,1)
array.SetElement(2,1)

print ("arr 2 is ",array)