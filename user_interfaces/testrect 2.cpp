#include <fstream>
#include <iostream>
#include "rect.hpp"

using namespace std;

int main()
{
    Rectangle A(5, 5, 0, 0);
    cout << "A: area is " << A.area() << " and perimeter is " << A.perimeter() << endl;
    Rectangle B(7, 8, 0, 0);
    cout << "B: area is " << B.area() << " and perimeter is " << B.perimeter() << endl;
}