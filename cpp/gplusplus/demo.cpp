#include "ai.h"
#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
    AI robot(2);
    cout << robot.ID() << endl;
    return 0;
}