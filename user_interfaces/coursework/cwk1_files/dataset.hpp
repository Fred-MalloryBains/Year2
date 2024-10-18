// COMP2811 Coursework 1: QuakeDataset class

#pragma once

#include <vector>
#include <iostream>
#include <fstream>
#include "quake.hpp"

using namespace std;

class QuakeDataset
{
public:
  // Specify prototypes or inlined methods here
  // (see UML diagram for what is required)
  QuakeDataset() = default;
  QuakeDataset(const string &filename);
  void loadData(const std::string &filename);
  Quake operator[](int index)
  {
    if (index < 0 || index >= data.size())
    {
      throw invalid_argument("index out of range");
    }
    return data[index];
  }
  int size()
  {
    return data.size();
  }
  Quake strongest();
  Quake shallowest();
  double meanDepth();
  double meanMagnitude();

private:
  std::vector<Quake> data;
};
