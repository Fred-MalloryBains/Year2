#pragma once

class Rectangle
{
private:
    double x;
    double y;
    double width;
    double height;

public:
    Rectangle(double x, double y, double width, double height)
    {
        this->x = x;
        this->y = y;
        this->width = width;
        this->height = height;
    }
    Rectangle(double width, double height)
    {
        double x = 0;
        double y = 0;
        double width = width;
        double hieght = height;
    }

    double get_x()
    {
        return x;
    }
    double get_y()
    {
        return y;
    }
    double get_width()
    {
        return width;
    }
    double get_height()
    {
        return height;
    }
};