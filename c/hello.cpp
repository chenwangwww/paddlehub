#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

bool compare(int a, int b)
{
    return a > b;
}
bool compare(double a, double b)
{
    return a > b;
}
int main()
{
    // compare(10,20);
    // compare(10.3,21.0);

    // int array[10] = {1,2};
    // int (*p)[10] = &array;
    // int (&q)[10] = array;
    // cout << (*p)[1] << endl;
    // cout << q[0] << endl;
    // cout << sizeof(int) << endl;

    // const char* format1 = "%s %d\n";
    // printf(format1, "hello", 10, 1);
    // printf_s(format1, "hello", 10, 1);

    // const char* format2 = "%s %d %d %d %s\n";
    // printf(format2, "hello", 10, 1);
    // printf_s(format2, "hello", 10, 1);
    return 0;
}