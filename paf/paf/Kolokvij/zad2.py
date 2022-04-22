import ProjectileDrop as pa
import numpy as np
import math
import matplotlib.pyplot as plt
p2=pa.ProjectileDrop()
p2.set_initial_conditions(100,100)
print(p2.change_y(75))
p3=pa.ProjectileDrop()
p3.set_initial_conditions(75,75)
print(p2.change_vx(30))