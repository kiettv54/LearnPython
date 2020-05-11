# Python3 program to process 
# images using skikit-image 
import os
import skimage

# way to load car image from file 
file = os.path.join(skimage.data_dir, 'beans.jpg') 

cars = io.imread(file) 

# way to show the input image 
io.imshow(cars) 
io.show() 
