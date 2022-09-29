import matplotlib.pyplot as plt
import numpy as np

x_data = np.arange(1, 70)
y_data = x_data+np.random.rand(x_data.shape[0])
linear_1 = 1.5*x_data
linear_2 = 0.5*x_data
log_1 = 2*np.log(x_data)
log_2 = 6*np.log(x_data)

# plt.plot(x_data, y_data, 'o', label="y label")
plt.plot(x_data, linear_1, label="linear 1")
plt.plot(x_data, linear_2, label="linear 2")
plt.plot(x_data, log_1, label="logarithmic 1")
plt.plot(x_data, log_2, label="logarithmic 2")
plt.legend(loc="best")
plt.xlabel("x data")
plt.ylabel("y data")
plt.savefig("function_linear_log.pdf")
