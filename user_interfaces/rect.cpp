#include <stdexcept>
#include "rect.hpp"
#include <iostream>
#include <fstream>

using namespace std;

Rectangle ::Rectangle(double width, double height, double x, double y) : width(width), height(height), x(x), y(y)
{
    if (width < 0.0 || height < 0.0)
    {
        throw invalid_argument("dimensions cannot be less than zero");
    }
}