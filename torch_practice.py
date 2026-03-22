import torch

# Create a 3-dimensional tensor. Tensors are arrayt hat can be saved in GPU as well along with CPU
images = torch.rand((4, 28, 28))

# Get the second image
second_image = images[2]

import matplotlib.pyplot as plt

plt.imshow(second_image, cmap='gist_rainbow')
plt.axis('off') # disable axes
plt.show()