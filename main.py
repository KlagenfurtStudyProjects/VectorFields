import matplotlib.pyplot as plt
import numpy as np
import math
import sys

def VanDerPolFunc(x1: int, x2: int) -> np.array:
    values: list[int] = []

    x: int = x2
    y: int = x2*(1 - x1**2) - x1
    values.append(x)
    values.append(y)

    return np.array(values)

def GetNorm(f: np.array) -> np.array:
    norm: float = math.sqrt(f[0]**2 + f[1]**2) #find norm
    return np.array([f[0] / norm, f[1] / norm]) # return unit vector

def Create2DGrid(a1: int, a2: int, b1: int, b2: int, k1: int, k2: int) -> np.array:
    fullGreed: list[int] = []

    horStepSize: int = (b1 - a1) / k1
    vertStepSize: int = (b2 - a2) / k2

    for i in range(k1+1):
        for j in range(k2+1):
            greedPoint: tuple[int, int] = (a1 + i*horStepSize, a2 + j*vertStepSize)
            fullGreed.append(greedPoint)
    
    return np.array(fullGreed)

grid: np.array = Create2DGrid(-5, -5, 5, 5, 20, 20)

x0_values: list = []
y0_values: list = []
dx_values: list = []
dy_values: list = []

for i in grid:
    x0: int = i[0]
    y0: int = i[1]
    func: np.array = VanDerPolFunc(x0, y0)
    norm: np.array = GetNorm(func)

    x0_values.append(x0)
    y0_values.append(y0)
    dx_values.append(norm[0])
    dy_values.append(norm[1])

plt.figure(figsize=(20, 20))
plt.title("Van der Pol Vector Field")
#vectors
plt.quiver(x0_values, y0_values, dx_values, dy_values, scale=40, color='g', label='Van der Pol Vector Field')
#points
plt.scatter(x0_values, y0_values, color='r', label='Initial Points')

plt.xlabel('x')
plt.ylabel('y')
# plt.legend(loc='lower center')
plt.grid(True)
plt.show()