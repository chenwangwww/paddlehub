#include <iostream>
#include <string>
#include <limits>
#include <typeinfo>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>

using namespace std;

// template <typename T> inline T const& Max(T const& a, T const& b)
// {
//     cout<<&a << ", " << &b <<endl;
//     return a<b?b:a;
// }
extern int count;
extern int max(int a, int b);
int sum(int a, int b = 20)
{
    int result;
    result = a + b;
    return result;
}

// template <typename T> inline T const& Max(T const& a, T const& b);

int main()
{
    // int i = 39;
    // int j = 20;
    // cout << &j << ", " << &i << endl;
    // Max(i, j);

    // cout << sizeof(bool) << endl;
    // cout << (numeric_limits<bool>::max)() << endl;
    // cout << (numeric_limits<bool>::min)() << endl;
    // cout << typeid((string)("ssss")).name() << endl;
    // cout << sizeof(short) << endl;
    // cout << sizeof(wchar_t) << endl;

    // enum color{red = 1, green, blue}c;
    // c = blue;
    // cout<<c;
    // cout<< 2.e-2;
//     const char a[] = "hello \
// dear";
//     const char b[] = "hello, " "d" "ear";
//     cout<<a<<endl;
    // cout<<b<<endl;

    // count = 23;
    // cout<<count<<endl;
    // cout << max(3,14) <<endl;

    // cout << sum(100);

    // auto basicLambda = []{cout << "hello, world!" << endl;};
    // basicLambda();

    // int x = 10;
    // auto add_x = [x](int a)mutable{x *=2;return a+x;};
    // cout<<add_x(10);

    // int a[] = {45,12,34,77,90,11,2,4,5,55};
    // sort(a, a + 10, [](int a, int b){return abs(a)>abs(b);});
    // for (int i = 0; i < 10; i++)
    // {
    //     cout<<a[i]<<" ";
    // }
    
    // double d = 30949.364;
    // cout<<sizeof(d);
    // cout<<sin(3.1415926/6);

    // int i,j;
    // srand((unsigned)time(NULL));
    // for (i = 0; i < 10; i++)
    // {
    //     j = rand();
    //     cout<<j<<endl;
    // }

    // double balance[10];
    // int a[3][2] = {{0,0},{1,2},{3,4}};
    // cout<<a[1][0];

    // char greeting[6] = {'h','e','l','l','o','\0'};
    // cout<<end(greeting)-begin(greeting)<<endl;
    // cout<<strlen(greeting);

    // char str1[11] = "hello";
    // char str2[11] = "world";
    // char str3[2] = "c";

    // // strcpy(str3, str1);
    // strcat(str3, str1);
    // cout<<str3<<endl;
    // cout<<strlen(str3)<<endl;
    // cout<<end(str3)-begin(str3)<<endl;

    // int var; int *ptr; int **pptr;
    // var = 3000; ptr = &var; pptr = &ptr;
    // cout<<var<<endl;
    // cout<<*ptr<<endl;
    // cout<<**pptr<<endl;

    int a = 13;
    cout<<double(a)/3;

    return 0;
}

// template <typename T> inline T const& Max(T const& a, T const& b)
// {
//     cout<<&a << ", " << &b <<endl;
//     return a<b?b:a;
// }