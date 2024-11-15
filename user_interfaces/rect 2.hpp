#pragma once

class Rectangle
{
private:
    double const x, y, width, height;

public:
    Rectangle(double, double, double, double);
    double get_x() const { return x; }
    double get_y() const { return y; }
    double get_width() const { return width; }
    double get_height() const { return height; }
    double perimeter() const { return 2 * (width + height); }
    double area() const { return width * height; }
};