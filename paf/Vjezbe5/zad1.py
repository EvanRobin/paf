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

p_an = har.HO()
p_an.set_initial_conditions(5, 1, 5, 0.005)

t1, x1, v1, a1 = p1.journey(10)
t2, x2, v2, a2 = p2.journey(10)
t3, x3, v3, a3 = p3.journey(10)
t4, x4, v4, a4 = p4.journey(10)
t_an, x_an, v_an, a_an = p_an.analitical()

plt.scatter(t1, x1, s=1)
plt.scatter(t2, x2, s=2)
plt.scatter(t3, x3, s=3)
plt.scatter(t4, x4, s=4)
plt.plot(t_an, x_an, "yellow")
plt.show()

plt.scatter(t1, v1, s=1)
plt.scatter(t2, v2, s=2)
plt.scatter(t3, v3, s=3)
plt.scatter(t4, v4, s=4)
plt.plot(t_an, v_an, "yellow")
plt.show()

plt.scatter(t1, a1, s=1)
plt.scatter(t2, a2, s=2)
plt.scatter(t3, a3, s=3)
plt.scatter(t4, a4, s=4)
plt.plot(t_an, a_an, "yellow")
plt.show()