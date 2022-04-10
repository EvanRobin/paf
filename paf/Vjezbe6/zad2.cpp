#include <iostream>
void radius(float r,float xc,float yc, float x,float y){
float xd;
xd= x-xc;
float yd;
yd= y-yc;
float rdot;
rdot=yd*yd+xd*xd;
if (rdot==r) {
    std::cout<<"Tocka se nalazi na kruznici";
    } else if (rdot<r) {
    std::cout<<"Tocka se nalazi u kruznici";   
    } else {
    std::cout<<"Tocka se nalazi van kruznici";
    }

}

int main(){

radius(1,1,1,1,1);

return 0;
}
