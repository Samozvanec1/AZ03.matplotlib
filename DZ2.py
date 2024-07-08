import numpy as np
import matplotlib.pyplot as plt

random_array = np.random.rand(5)
print(random_array)

y = np.random.rand(5)

plt.scatter(random_array,y)

plt.title("Диаграмма случайная создана мной (М.Й.)")
plt.xlabel("random_array")
plt.ylabel("специальный массив")
plt.show()