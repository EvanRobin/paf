// C++ Implementation to find the line passing
// through two points
#include <iostream>
using namespace std;
 
// This pair is used to store the X and Y
// coordinate of a point respectively
#define pdd pair<double, double>
 
// Function to find the line given two points
void lineFromPoints(pdd P, pdd Q)
{
    double a = Q.second - P.second;
    double b = P.first - Q.first;
    double c = a * (P.first) + b * (P.second);
 
    if (b < 0) {
        cout << "The line passing through points P and Q "
                "is: "
             << a << "x - " << b << "y = " << c << endl;
    }
    else {
        cout << "The line passing through points P and Q "
                "is: "
             << a << "x + " << b << "y = " << c << endl;
    }
}
 
// Driver code
int main()
{
    pdd P = make_pair(3, 2);
    pdd Q = make_pair(2, 6);
    lineFromPoints(P, Q);
    return 0;
}