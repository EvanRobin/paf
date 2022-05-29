#include <iostream>
#include <Particle.h>

int main()
{
    Particle p1(1.0, 0.5, 0.0, 0.0);
    p1.range();
    p1.time();

    Particle p2(3.0, 0.3, 5.0, 5.0);
    p2.range();
    p2.time();
    return 0;
}