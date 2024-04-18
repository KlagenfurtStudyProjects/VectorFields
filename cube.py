import matplotlib.pyplot as plt
import numpy as np
import math
import sys


def PointCharge(vector: np.array) -> np.array:
    values: list[int] = []

    Q: int = 1
    PI: float = math.pi
    E0: float = 8.854e-12
    NORM: float = math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    multiplier: float = Q / (4*PI*E0*NORM)

    for i in vector:
        values.append(i*multiplier)

    return np.array(values)

def GetNorm(f: np.array) -> np.array:
    norm: float = math.sqrt(f[0]**2 + f[1]**2 + f[2]**2) #find norm
    return np.array([f[0] / norm, f[1] / norm, f[2] / norm]) # return unit vector

def Create3DGrid(a1: int, a2: int, a3:int, b1: int, b2: int, b3: int, k1: int, k2: int, k3: int) -> np.array:
    fullGreed: list[int] = []

    horStepSize: int = (b1 - a1) / k1
    vertStepSize: int = (b2 - a2) / k2
    zStepSize: int = (b3 - a3) / k3

    for i in range(k1+1):
        for j in range(k2+1):
            for k in range(k3+1):
                greedPoint: tuple[int, int, int] = (a1 + i*horStepSize, a2 + j*vertStepSize, a3 + k*zStepSize)
                fullGreed.append(greedPoint)
    
    return np.array(fullGreed)

grid: np.array = Create3DGrid(-1, -1, -1, 1, 1, 1, 10, 10, 10)

x0_values: list = []
y0_values: list = []
z0_values: list = []
dx_values: list = []
dy_values: list = []
dz_values: list = []

for i in grid:
    x0: float = i[0]
    y0: float = i[1]
    z0: float = i[2]
    # skip (0, 0, 0) point
    if x0 == 0 and y0 == 0 and z0 == 0:
        continue
    func: np.array = PointCharge(np.array([x0, y0, z0]))
    norm: np.array = GetNorm(func)

    x0_values.append(x0)
    y0_values.append(y0)
    z0_values.append(z0)
    dx_values.append(norm[0])
    dy_values.append(norm[1])
    dz_values.append(norm[2])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(x0_values, y0_values, z0_values, dx_values, dy_values, dz_values, color = "red", length=0.1, normalize=True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Vector Field')

plt.show()