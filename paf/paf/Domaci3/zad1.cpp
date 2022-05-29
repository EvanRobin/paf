#include "matplotlibcpp.h"
namespace plt=matplotlibcpp.h;
int main()
{
    plt::plot({1,2,3,4},"*");
    plt::show();
}
//g++ zad1.cpp -std=c++11 -I/usr/include/python3.10 -lpython3.10