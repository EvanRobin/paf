import oscilator as har
import matplotlib.pyplot as plt

p1 = har.HO()
p2 = har.HO()
p3 = har.HO()
p4 = har.HO()

p1.set_initial_conditions(5, 1, 5, 0.01)
p2.set_initial_conditions(5, 1, 5, 0.05)
p3.set_initial_conditions(5, 1, 5, 0.25)
p4.set_initial_conditions(5, 1, 5, 0.5)

print(p1.period())
print(p2.period())
print(p3.period())
print(p4.period())