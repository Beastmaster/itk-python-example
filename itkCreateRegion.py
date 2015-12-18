# Author: QIN Shuo
# Date:   2015/10/26
# This is a test file for itk
# This example demonstrates how to create a region in ITK
# Only 2/3 dimensions (dimensions depend on your choice in cmake when compiling ITK)



import itk

# set start position 
startID_2 = [0,0]    # for 2D region
startID_3 = [0,0,0]  # for 3D region

# set region size
size_2 = [100,100]         # for 2D region
size_3 = [100,100,100]     # for 3D region


# describe a region
region_2 = itk.ImageRegion._2(startID_2,size_2)   #2D region
region_3 = itk.ImageRegion._3(startID_3,size_3)   #3D region


