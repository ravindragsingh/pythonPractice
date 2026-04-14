'''
Matplotlib is a popular Python library used for creating static, interactive, and animated visualizations.
It is widely used in data science, machine learning, and scientific computing to visualize data and results.
What is pyplot?
pyplot is a module in Matplotlib that provides a collection of functions for creating plots and visualizations.
These functions allow you to easily generate various types of plots, such as line plots, bar plots, scatter plots, and histograms, with a high-level interface.
'''

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

'''plt.plot(x, y)  # Create a line plot
plt.title("Line Plot")  # Add a title
plt.xlabel("X-axis")  # Label the x-axis
plt.ylabel("Y-axis")  # Label the y-axis
plt.show()  # Display the plot
'''
import numpy as np

img = np.random.random((10, 10))  # Create a random image
plt.imshow(img, cmap='gist_rainbow')  # Display the image in grayscale
plt.colorbar()  # Add a colorbar
plt.show()

'''
plt.scatter([1, 2, 3],[1, 3, 5] )  # Create a scatter plot
plt.show()
'''