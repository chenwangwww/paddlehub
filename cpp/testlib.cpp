#include "testlib.h"

__declspec(dllexport) int __stdcall Add(int a, int b)
{
    return a + b;
}