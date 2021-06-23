#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        a=(self.radius**2)*np.pi
        return a
small_circle=circle(1)
print(small_circle.area())
c=3e8


# In[18]:


class space_ship:
    def __init__(self,init_mass,speed,color,engine,capacity):
        self.mass=init_mass
        self.speed=speed
        self.color=color
        self.engine=engine
        self.capacity=capacity
    def rel_mass(self):
        m=self.mass/np.sqrt(1-(self.speed**2/c**2))
        return m
small_space_ship=space_ship(1000,20000,"red","electric","15people")
print("my space ship is" ,small_space_ship.color,",it's engine is",small_space_ship.engine,",it has capacity",small_space_ship.capacity,",it relative mass is",small_space_ship.rel_mass(),"kg,when it is at the speed of",small_space_ship.speed,"km per hour")
        


# In[ ]:




