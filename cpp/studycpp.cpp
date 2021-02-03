#include <functional>
#include <iostream>
#include <list>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

// template <class T> class is_odd
// {
//     public:
//         bool operator()(T& val)
//         {
//             return (val % 2) == 1;
//         }
// };
// template <class A, class B> class MyMap;
// template <class B> class MyMap<std::string, B>;

// template <class A, class B> class MyMap{
//     public:
//         MyMap();
// };
// template<class A, class B> MyMap<A, B>::MyMap(){
//     cout << "mymap!" << endl;
// }

// template <class B> class MyMap<std::string, B>{
//     public:
//         MyMap();
// };
// template<class B> MyMap<string, B>::MyMap(){
//     cout << "partial!" << endl;
// }

// class Box
// {
// private:
    
// public:
//     Box(/* args */);
//     ~Box();
// };

// Box::Box()
// {
//     cout<<"box!";
// }

// Box::~Box()
// {
// }

// template<class T> void f(T){
//     if (typeid(T) == typeid(char))
//     {
//         cout << "dara";
//     }else{
//         cout << "wrong!";
//     }
    
// }

// template<class T, int i> class MyStack
// {
//     public:
//         T* pStack;
//         T StackBuffer[i];
//         static const int cItems = i * sizeof(T);

//     public:
//         MyStack();
//         void push(const T item);
//         T& pop();
// };

// template<class T, int i>MyStack<T,i>::MyStack()
// {
//     memset(StackBuffer, 0, sizeof(StackBuffer));
//     pStack = StackBuffer;
//     pStack--;
//     for(auto item : StackBuffer){
//         cout << item << " ";
//     }
//     cout << endl;
// }
// template<class T, int i> void MyStack<T,i>::push(const T item)
// {
//     if((pStack - StackBuffer) == (i-1)){
//         cout << "over" << endl;
//         return;
//     }
//     pStack++;
//     *pStack = item;
// }
// template<class T, int i> T& MyStack<T,i>::pop()
// {
//     if((++pStack) == StackBuffer){
//         --pStack;
//         return StackBuffer[0];
//     }
//     T a = *pStack;
//     *pStack = 0;
//     pStack--;
//     return a;
// }

// template<class T> class X
// {
//     template<class U> class Y
//     {
//         U* u;
//         public:
//             Y();
//             U& Value();
//             void print();
//             ~Y();
//     };

//     Y<int> y;
//     public:
//         X(T t){
//             y.Value() = t;
//         }
//         void print(){y.print();}
// };

// template<class T> template<class U> X<T>::Y<U>::Y()
// {
//     cout << "X<T>::Y<U>::Y()" << endl;
//     u = new U();
// }

// template <class T>
// template <class U>
// U& X<T>::Y<U>::Value()
// {
//    return *u;
// }

// template <class T>
// template <class U>
// void X<T>::Y<U>::print()
// {
//    cout << this->Value() << endl;
// }

// template <class T>
// template <class U>
// X<T>::Y<U>::~Y()
// {
//    cout << "X<T>::Y<U>::~Y()" << endl;
//    delete u;
// }

// template<class T> class Array;
// template<class T> void f(Array<T>& a);

// template<class T> class Array
// {
//     T* array;
//     int size;

//     public:
//         Array(int sz): size(sz){
//             array = new T[size];
//             memset(array, 0, size * sizeof(T));
//         }
//         Array(const Array& a){
//             size = a.size;
//             array = new T[size];
//             memcpy(array, a.array, size * sizeof(T));
//         }
//         T& operator[](int i){
//             return *(array + i);
//         }
//         int Length(){return size;}
//         void print(){
//             for(int i = 0; i < size; i++)
//                 cout << *(array + i) << " ";
//             cout << endl;
//         }
//         ~Array(){
//             delete array;
//             array = NULL;
//         }
//         template<class U> friend Array<U>* combine(Array<U>& a1, Array<U>& a2);
//         friend void f<>(Array<T>& a);
// };

// template<class T> Array<T>* combine(Array<T>& a1, Array<T>& a2)
// {
//     Array<T>* a = new Array<T>(a1.size + a2.size);
//     for (size_t i = 0; i < a1.size; i++)
//     {
//         (*a)[i] = *(a1.array + i);
//     }
//     for (size_t i = 0; i < a2.size; i++)
//     {
//         (*a)[i + a1.size] = *(a2.array + i);
//     }
//     return a;  
// }

// template<class T> void f(Array<T>& a)
// {
//     cout << a.size << " generic" << endl;
// }

// template<> void f(Array<int>& a)
// {
//     cout << a.size << " int" << endl;
// }

// template<class T> class X
// {
//     private:
//         T* data;
//         void InitData(int seed){data = new T(seed);}
//     public:
//         void print(){cout << *data << endl;}
//         template<class U> friend class Factory;
// };

// template<class U> class Factory
// {
//     public:
//         U* GetNewObject(int seed)
//         {
//             U* pu = new U;
//             pu->InitData(seed);
//             return pu;
//         }
// };

// template<class T> void MySwap(T& a, T& b){
//     T c(a);
//     a = b;
//     b = c;
// }

// struct X
//     {
//         X(const int& a, int& b){
//             cout << a << "," << b << endl;
//         }
//     };

class MemoryBlock
{
    public:
     int a = 5;
};

void f(const MemoryBlock& a)
{
    cout << "const MemoryBlock&" << a.a << endl;
}

void f(MemoryBlock&& a)
{
    a.a = 11;
    cout << "MemoryBlock&&" << a.a << endl;
}

int main()
{
    MemoryBlock block;
    f(block);
    f(MemoryBlock());

    // int a = 3;
    // X* p = new X(1,a);
    // delete p;
    // Factory<X<int>> XintFactory;
    // X<int>* x1 = XintFactory.GetNewObject(65);
    // X<int>* x2 = XintFactory.GetNewObject(97);

    // Factory<X<char>> XcharFactory;
    // X<char>* x3 = XcharFactory.GetNewObject(65);
    // X<char>* x4 = XcharFactory.GetNewObject(97);
    // x1->print();
    // x2->print();
    // x3->print();
    // x4->print();

    // Array<char> ac(10);
    // f(ac);

    // Array<int> a(10);
    // f(a);

    // Array<char> alpha1(26);
    // for (size_t i = 0; i < alpha1.Length(); i++)
    // {
    //     alpha1[i] = 'A' + i;
    // }
    // alpha1.print();

    // Array<char> alpha2(26);
    // for (size_t i = 0; i < alpha2.Length(); i++)
    // {
    //     alpha2[i] = 'a' + i;
    // }
    // alpha2.print();

    // Array<char>* alpha3 = combine(alpha1, alpha2);
    // alpha3->print();
    // delete alpha3;

    // Array<int> alpha1(26);
    // alpha1[0] = 11;
    // alpha1[1] = 12;
    // Array<int> alpha2(alpha1);
    // cout << alpha2[1];

    // Array<char> alpha1(26);
    // alpha1[0] = 'A';
    // alpha1[1] = 'A';
    // Array<char> alpha2(alpha1);
    // cout << alpha2[1];

    // X<int> xi = X<int>(10);
    // X<char>* xc = new X<char>('c');
    // xi.print();
    // xc->print();
  
    // delete xc;
    // f<int>(10);
    // MyStack<int, 5> m;
    // m.push(1);
    // m.push(2);
    // m.push(2);
    // m.push(2);
    // m.push(2);
    // for(auto item : m.StackBuffer){
    //     cout << item << " ";
    // }
    // cout << endl;
    // cout << m.pop() << endl;
    // cout << m.pop() << endl;
    // auto f1 = [](int x, int y){return x+y;};
    // cout << f1(2,4) <<endl;
    // function<int(int, int)> f2 = [](int x, int y){return x+y;};
    // cout << f2(3,7) <<endl;

    // int i = 3;
    // int j = 5;
    // function<int()> f = [i, &j](){return i + j;};
    // i = 22;
    // j = 33;
    // cout << f() << endl;

    // list<int> c1;
    // c1.push_back(4);
    // c1.push_back(19);
    // cout << c1.size() << endl;
    // int& i = c1.back();
    // cout << i << c1.size() << endl;
    // i = 12;
    // cout << c1.back() << endl;

    // list<string> c2;
    // string str("ab");
    // c2.emplace(c2.begin(), str);
    // cout << c2.back() << endl;

    // list<int> c1;
    // list<int>::iterator c1_iter;
    // c1.push_back(10);
    // c1.push_back(20);
    // c1.push_back(30);
    // c1_iter = c1.end();
    // printf("%#X\n", c1_iter);
    // c1_iter--;
    // cout << *c1_iter << endl;
    // printf("%#X", c1_iter);

    // list<string> c1;
    // list<string>::iterator c1_iter, c2_iter;
    // c1.push_back("5");
    // c1.push_back("100");
    // c1.push_back("5");
    // c1.push_back("200");
    // c1.push_back("5");
    // c1.push_back("300");
    // for (c1_iter = c1.begin(); c1_iter != c1.end(); c1_iter++)
    // {
    //     cout << *c1_iter << "   " ;
    // }
    // cout << endl;

    // list<string> c2 = c1;
    // c2.remove("5");
    // for ( c2_iter = c2.begin(); c2_iter != c2.end(); c2_iter++)
    // {
    //     cout << *c2_iter << "   ";
    // }
    // cout << endl;

    // for (c1_iter = c1.begin(); c1_iter != c1.end(); c1_iter++)
    // {
    //     cout << *c1_iter << "   " ;
    // }
    // cout << endl;

    // auto f = is_odd<int>();
    // int x = 4;
    // cout << f(x);

    // list<int> c2;
    // c2.push_back(10);
    // c2.pop_back();

    // list<int> c1, c2;
    // c1.push_back(10);
    // c1.push_back(20);
    // c1.push_back(30);
    // c2.push_back(40);
    // c2.push_back(50);
    // c2.push_back(60);

    // cout << "c1=";
    // for(auto c:c1)
    //     cout << "   " << c;
    // cout << endl;

    // c1.assign(++c2.begin(), c2.end());
    // cout << "c1=";
    // for(auto c:c1)
    //     cout << "   " << c;
    // cout << endl;

    // c1.assign(2,4);
    // cout << "c1=";
    // for(auto c:c1)
    //     cout << "   " << c;
    // cout << endl;

    // c1.assign({10,20,30,40});
    // cout << "c1=";
    // for(auto c:c1)
    //     cout << "   " << c;
    // cout << endl;

    // list<int>::value_type anint;
    // cout << anint;

    // list<int> c1;

    // c1.push_back(-10);
    // c1.push_back(10);
    // c1.push_back(10);
    // c1.push_back(20);
    // c1.push_back(20);
    // c1.push_back(-10);

    // c1.unique();
    // for(auto c:c1){
    //     cout << c << "  ";
    // }

    // vector<int> v1, v2;
    // v1.push_back(10);
    // v1.push_back(20);
    // v2.push_back(50);
    // swap(v1, v2);
    // for(int c : v1){
    //     cout << c << "  ";
    // }
    // cout << endl;

    // for(int v : v2){
    //     cout << v << "  ";
    // }
    // cout << endl;

    // vector<int> c1;
    // vector<int>::pointer c1_ptr;
    // vector<int>::const_pointer c1_cptr;

    // c1.push_back(1);
    // c1.push_back(2);

    // c1_cptr = c1.data();
    // for(size_t n = c1.size(); 0<n; --n,c1_cptr++,cout<<"ss  ")
    // {
    //     cout << c1_cptr << "   ";
    // }
    // cout << endl;

    // c1_ptr = c1.data();
    // *c1_ptr = 20;
    // for(size_t n = c1.size();0<n;--n,c1_ptr++)
    // {
    //     cout << c1_ptr << "    ";
    // }
    // cout << endl;

    // vector<int> c1;
    // vector<int>::iterator c1_iter;
    // c1.push_back(1);
    // c1_iter = c1.begin();
    // printf("%#X\n", c1_iter);
    // printf("%#X\n", c1.end());
    // cout << c1[0];

    // vector<bool> vb = {true, false, false};
    // for(const auto& b:vb){
    //     cout << b << "  ";
    // }
    // cout << endl;

    // // vb.flip();
    // for(auto b:vb){
    //     b = !b;
    // }
    // for(const auto& b:vb){
    //     cout << b << "  ";
    // }
    // cout << endl;
    // vb.erase(vb.begin());
    // cout << vb.size();
    // cout << endl;
    // for(const auto& b:vb){
    //     cout << b << "  ";
    // }
    // cout << endl;

    // vector<int> vec{0,1,2,3,4};
    // vector<int>::iterator iter = begin(vec);
    // iter++;
    // cout << *iter << endl;
    // *iter--;
    // cout << *iter << endl;
    // for(auto lt:vec)
    // {
    //     cout << lt << "    ";
    // }

    // size_t t;

    // MyMap<int, char> map1;
    // MyMap<string, int> map2;
    // Box b;

    
}

