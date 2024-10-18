// COMP2811 Coursework 1: QuakeDataset class
#include <vector>
#include <iostream>
#include <fstream>
#include "dataset.hpp"
#include "csv.hpp"

using namespace std;

QuakeDataset::QuakeDataset(const string &filename)
{
    loadData(filename);
}

void QuakeDataset::loadData(const string &filename)
{
    ifstream infile(filename);
    if (not infile)
    {
        throw invalid_argument("no such file ");
    }
    csv::CSVReader reader(filename);
    for (auto &row : reader)
    {
        string time;
        double lon, lat, mag, dep;
        try
        {
            string time = row["time"].get<>();
            double lat = row["latitude"].get<double>();
            double lon = row["longitude"].get<double>();
            double dep = row["depth"].get<double>();
            double mag = row["mag"].get<double>();
            data.push_back(Quake(time, lat, lon, dep, mag));
        }
        catch (const std::exception &e)
        {
            throw invalid_argument("Unable to read row data: " + string(e.what()));
        }
    }
}
Quake QuakeDataset::strongest()
{
    if (data.size() == 0)
    {
        throw invalid_argument("no data ");
    }
    int max = -1;
    int pointer = -1;
    for (int i = 0; i < data.size(); i++)
    {
        if (data[i].getDepth() > max)
        {
            max = data[i].getDepth();
            pointer = i;
        }
    }
    return data[pointer];
}
Quake QuakeDataset::shallowest()
{
    if (data.size() == 0)
    {
        throw invalid_argument("no data ");
    }
    int min = 100;
    int pointer = -1;
    for (int i = 0; i < data.size(); i++)
    {
        if (data[i].getDepth() < min)
        {
            min = data[i].getDepth();
            pointer = i;
        }
    }
    return data[pointer];
}
double QuakeDataset::meanDepth()
{
    if (data.size() == 0)
    {
        throw invalid_argument("empty dataset ");
    }

    double mean_dep = 0;
    for (int i = 0; i < data.size(); i++)
    {
        mean_dep += data[i].getDepth();
    }
    return mean_dep / data.size();
}
double QuakeDataset::meanMagnitude()
{
    if (data.size() == 0)
    {
        throw invalid_argument("empty dataset ");
    }
    double mean_mag = 0;
    for (int i = 0; i < data.size(); i++)
    {
        mean_mag += data[i].getMagnitude();
    }
    return mean_mag / data.size();
}