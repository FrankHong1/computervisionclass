#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import numpy as np
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        a=(radius**2)*np.pi
        return a
small_circle=circle(1)
print(small_circle.area)


