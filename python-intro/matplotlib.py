import matplotlib
import numpy as np
import matplotlib.pyplot as plt


# Plot a linear function
# Note: range(upperlimit) function creates an array of integers in the interval [0, upperlimit)

x = np.array(range(10))
double_x = 2*x
plt.plot(x,double_x)
plt.show() # this line is necessary for the figure to appear as a window in the screen. If it is missing, the plot will be created, but not shown

def my_fun(x):
    return x

print(my_fun(x))

# Plot a hyperbolic function

x = np.arange(-10,10,0.2)
square_x = x**2
plt.plot(x,square_x)
plt.show()


# Add axis labels, limits, title, legend

plt.plot(x,square_x, label = 'legend')
plt.xlim([-7.0, 7.0])
plt.ylim([-1, 30.0])
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Example curve')
plt.legend(loc = 'upper right')
plt.show()
# Plot 2 curves on the same figure

x_cube = x ** 3
plt.plot(x,square_x, label = 'x^2')
plt.plot(x,x_cube, label = 'x^3')
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Example curve')
plt.legend(loc = 0) # loc=0 automatically decides which is the best location to place the legend
plt.show()


# Plot a scatter plot for 2 randomly generated arrays (note that the arrays should have the same size)

x = np.random.rand(200)
y = np.random.rand(200)
plt.scatter(x,y, c='#009999')
plt.show()


# # Load an image

loaded_image = plt.imread('train.png')
type(loaded_image)
print('The loaded image is of type: ' + str(type(loaded_image)) + ', and of shape: ' + str(loaded_image.shape))


# The image is loaded as a numpy array, of *image dimensions* x *color channels*. Each color pixel is represented by a float value, taking values from 0 to 1.

print(loaded_image.dtype)
print('The image values are between ' + str(loaded_image.min()) + ' and ' + str(loaded_image.max()))
print('The image values are between ' + str(np.min(loaded_image)) + ' and ' + str(np.max(loaded_image)))


# Show the image

plt.imshow(loaded_image)
plt.show()


# Plot the 3 different color channels of the image in subplots

plt.subplot(1,3,1)
plt.imshow(loaded_image[:,:,0])
plt.axis('off') # this line removes the axis numbering
plt.title('Red')
plt.subplot(1,3,2)
plt.imshow(loaded_image[:,:,1])
plt.axis('off')
plt.title('Green')
plt.subplot(1,3,3)
plt.imshow(loaded_image[:,:,2])
plt.axis('off')
plt.title('Blue')
plt.show()


# Plot 1 channel with colorbar

plt.imshow(loaded_image[:,:,0])
plt.axis('off')
plt.title('Red')
plt.colorbar()
plt.show()


# Crop a part of the image

lower_left = loaded_image[200:, :200, :]
lower_left.shape


# Show the cropped part

plt.imshow(lower_left)
plt.show()
