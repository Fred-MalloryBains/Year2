#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void read_data(istream &input, vector<float> &data)
{
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

    return 0;
}