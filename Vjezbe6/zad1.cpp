

#include <iostream>
void pravac(float x1,float y1, float x2,float y2){
float p;
p = (y2-y1)/(x2-x1);
float l;
l=-p*x1+y1;
std::cout<<"y="<<p<<"x+"<<l<<std::endl;
}

int main(){

pravac(1,1,3,3);

return 0;
}
