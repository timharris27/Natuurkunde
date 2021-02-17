# Hoofdstuk 1

print('Hello World')

import numpy as np
import matplotlib.pyplot as plt
plt.ion()

data = np.random.randn(2, 100)
fig, ax = plt.subplots()
ax.scatter(*data, c=data[1], s=100*np.abs(data[0]));
ax.title.set_text('Mooi grafiekje')

