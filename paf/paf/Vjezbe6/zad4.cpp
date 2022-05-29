#include <iostream>

void sustav(float a1, float b1, float c1, float a2, float b2, float c2){
    float x, y;
    if (a1*b2 - b1*a2 == 0){
        std::cout << ".";
    }else{
        x = (c1*b2 - b1*c2)/(a1*b2 - b1*a2);
        y = (a1*c2 - c1*a2)/(a1*b2 - b1*a2);
        std::cout << "x = " << x << "\ny = " << y;
    }
}
int main(){
    sustav(2, 3, 4, 2, -1, 3);
}