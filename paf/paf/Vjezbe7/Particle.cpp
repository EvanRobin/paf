#include <Particle.h>
#include <math.h>
#include <iostream>
#include <cmath>
void Particle::evolve()
{
        vy += g*dt;
        x += vx*dt;
        y += vy*dt;
        t += dt;
    
}
double Particle::range()
{
    while(y >= 0){
        evolve();
    }
    std::cout << x << std::endl;
    return x;
}
double Particle::time()
{
    while(y >= 0){
        evolve();
    }
    std::cout << t << std::endl;
    return t;
}
Particle::Particle(double v, double angle, double x0, double y0)
{
    t = 0;
    angle = angle;
    v = v;
    vy = sin(angle) * v;
    vx = cos(angle) * v;
    x = x0; 
    y = y0;      
}