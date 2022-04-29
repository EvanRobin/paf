#include <Particle.h>
#include <math.h>

void Particle::evolve()
{
    while(y >= 0)
    {
        vx += 0.;
        vy += g*dt;

        x += vx*dt;
        y += vy*dt;

        t += dt;
    }
}