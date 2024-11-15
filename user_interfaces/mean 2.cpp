#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void read_data(istream &input, vector<float> &data)
{
    float value;
    while (input >> value)
    {
        data.push_back(value);
    }
    cout << data.size();
}

float mean_value(vector<float> &data)
{
    float sum = 0;
    for (float i : data)
    {
        sum += i;
    }
    return sum / data.size();
}
int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        cerr << "Usage: ./mean <filename>" << endl;
        return 1;
    }

    ifstream infile(argv[1]);
    if (not infile)
    {
        cerr << "Error: cannot access " << argv[1] << endl;
        return 2;
    }

    vector<float> data;

    read_data(infile, data);
    float mean = mean_value(data);

    cout << "size of file: " << data.size() << endl;
    cout << "mean value: " << mean << endl;

    return 0;
}