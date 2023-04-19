# Offset1D: A simple tool for plotting a quantity around a 1D surface
Using a set of points augmented with values of the quantity that is of interest, you can obtain a set of points, representing the graph of the quantity around the surface.


## How to use the code
To install the package, just use pip:
```bash
pip install offset1d
```

A simple example of the use for the package is following:

```python
import offset1d.getxy as getxy
import math
import random

N = 50
values = [random.uniform(-0.1,0.1) for k in range(N)]
values_on_circle = [(math.cos(k/N*2*math.pi), math.sin(k/N*2*math.pi), values[k]) for k in range(N)]
outline, graph = getxy.surf_and_graph(values_on_circle,scale=0)


import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(*outline,'black')
ax.plot(*graph,'red')
ax.set_aspect('equal')
plt.show()

```
Output:
![Example](./example.png)


You want to use the function *surf_and_graph* from the *getxy* module. The order of the points in the list passed to the function matters. The surface is created by connecting the points in the list as ordered in the list. Reversing the order of points does not affect the result.

### Scaling
The graph can be scaled around the 1D surface with the *scale* argument passed to the *surf_and_graph* function. If 0 is passed as the value (that is done by default), the graph height around the line is kept at the raw values. If scale is set to some positive constant *k*, the graph is scaled first to its maximum (or minimum) height above the surface to be equal to the surfaces' maximum width or height. Then it is scaled by the *scale* parameter. 

Example of an unscaled graph:
```python
import offset1d.getxy
import math

N = 200

values_on_circle = [
    (
    	math.sin(2*math.cos(k/N*2*math.pi)), 
    	math.sin(k/N*2*math.pi), 
     	0.01*(1+math.cos(k/N*6*math.pi))
    ) for k in range(N)
]
outline, graph = offset1d.getxy.surf_and_graph(values_on_circle)


import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(*outline,'black')
ax.plot(*graph,'red')
ax.set_aspect('equal')
plt.show()
```
![Unscaled graph](./example_unscaled.png)

You can set the scale to 1:
```python
...
offset1d.getxy.surf_and_graph(values_on_circle, scale=1)
...
```
![Scaled graph 1](./example_scaled_1.png)
The scale is to high for the curve is self-intersecting near the concave parts of the black surface. Smaller scale solves the problem.
```python
...
offset1d.getxy.surf_and_graph(values_on_circle, scale=0.2)
...
```
![Scaled graph 2](./example_scaled_2.png)


## Licence
You are free to use or modify the code under the [MIT licence](./LICENCE).