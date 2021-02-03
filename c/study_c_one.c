#include <stdio.h>

void main()
{
    volatile int i = 10;
    int a = i;
    printf("i = %d", a);
    // __asm {
    //     mov dword ptr [ebp-4], 20h
    // }

    int b = i;
    printf("i = %d", b);
}