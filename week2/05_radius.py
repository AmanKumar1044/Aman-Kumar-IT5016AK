"""
calculate the radius of  a circle, given the area
author: aman kumar
"""
import math
area = float(input("enter the area value:")) # input area value
radius = math.sqrt(area / math.pi)

print("radius of circle is",radius)