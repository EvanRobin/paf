from cgitb import reset
import ProjectileDrop as pa
import numpy as np
import math
import matplotlib.pyplot as plt
p6=pa.ProjectileDrop()
p7=pa.ProjectileDrop()
p6.set_initial_conditions(2000,200)
print(p6.DROPDABOMBMANgraf(7038,1,-100))
p7.set_initial_conditions(2000,200)
print(p7.DROPDABOMBMANgraf(7038,1,0))