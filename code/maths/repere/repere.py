import matplotlib.pyplot as plt
import numpy as np
import seaborn

seaborn.set(style="ticks")

x = np.linspace(-5, 5, 50)
y = np.zeros(50)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(y, x)
ax.set_aspect("equal")
ax.grid(True, which="both")
seaborn.despine(ax=ax, offset=0)  # the important part here
# plt.axis("equal")
plt.xticks(range(-5, 5))
plt.yticks(range(-5, 5))
plt.xlim([-5, 5])
plt.ylim([-5, 5])
plt.savefig("repere.pdf")
