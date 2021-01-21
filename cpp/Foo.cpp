#include <iostream>
#include <cassert>
#include <string>

using namespace std;

// void analyze_string(int s);
// constexpr int check_amount(const int n)
// {
//     return n;
// }

// class Foo1
// {
// private:
//     const int s2 = 10;
// public:
//     Foo1();
//     ~Foo1();
// };

// Foo1::Foo1()
// {
//     static_assert(check_amount(21) <= 22, "s2 is too large!");
// }

// Foo1::~Foo1()
// {
// }

// constexpr int calc(int n)
// {
//     if(n % 2 == 0){
//         return n * n;
//     }else{
//         return n * n + 1;
//     }
// }

// class CClass
// {
//     public:
//         constexpr explicit CClass(int n_) : n(n_){};
//         int n;
//         constexpr CClass operator*(const CClass& rhs) const{
//             return CClass(n * rhs.n);
//         }
// };

// constexpr CClass cube(CClass c1)
// {
//     return c1 * c1 * c1;
// }

// class IntVector {
// public:
//    IntVector( int cElements );
//    ~IntVector() { delete [] _iElements; }
//    int& operator[](int nSubscript);
// private:
//    int *_iElements;
//    int _iUpperBound;
// };

// // Construct an IntVector.
// IntVector::IntVector( int cElements ) {
//    _iElements = new int[cElements];
//    _iUpperBound = cElements;
// }

// // Subscript operator for IntVector.
// int& IntVector::operator[](int nSubscript) {
//    static int iErr = -1;

//    if( nSubscript >= 0 && nSubscript < _iUpperBound )
//       return _iElements[nSubscript];
//    else {
//       clog << "Array bounds violation." << endl;
//       return iErr;
//    }
// }

// const class mynullptr_t
// {
//    public:
//       template<class T> inline operator T *() const
//       {
//          cout << "T* is called" << endl;
//          return 0;
//       }
//       template<class C, class T> inline operator T C::*() const
//       {
//          cout << "T C::* is called" << endl;
//          return 0;
//       }
//    private:
//       void operator&() const;
// }mynullptr = {};

// class A{
//    public:
//       int *a;
// };

// template<class T> class complex{
//    T a, b;
//    public:
//       complex(T, T);
//       complex(){};
//       void show();
//       complex operator+(complex &);
//       complex operator-(complex &);
// };

// template<class T> complex<T>::complex(T x, T y):a(x), b(y){
//    cout << "have create the complex!" << endl;
// }

// template<class T> complex<T> complex<T>::operator+(complex<T> &x1)
// {
//    return complex(a + x1.a, b + x1.b);
// }

// template<class T> complex<T> complex<T>::operator-(complex<T> &x2)
// {
//    return complex(a-x2.a, b-x2.b);
// }

// template<class T> void complex<T>::show()
// {
//    cout << a << "," << b << endl;
// }

// class Int
// {
//    public:
//       Int& operator++();
//       void show();
//    private:
//       int _i;
// };

// Int& Int::operator++()
// {
//    _i++;
   
//    return *this;
// }

// void Int::show()
// {
//    cout << _i << endl;
// }

// class MyException{};
// class Dummy
// {
//    public:
//       Dummy(string s):MyName(s){PrintMsg("Create Dummy");}
//       Dummy(const Dummy& other): MyName(other.MyName){PrintMsg("copy Create Dummy");}
//       ~Dummy(){PrintMsg("destroy Dummy");}
//       void PrintMsg(string s){cout << s << MyName << endl;}
//       string MyName;
// };

// void C(Dummy d)
// {
//     cout << "Entering FunctionC" << endl;
//     d.MyName = " C";
//     throw MyException();

//     cout << "Exiting FunctionC" << endl;
// }

// void B(Dummy d)
// {
//     cout << "Entering FunctionB" << endl;
//     d.MyName = "B";
//     C(d);
//     cout << "Exiting FunctionB" << endl;
// }

// void A(Dummy d)
// {
//     cout << "Entering FunctionA" << endl;
//     d.MyName = " A" ;
//   //  Dummy* pd = new Dummy("new Dummy"); //Not exception safe!!!
//     try
//     {
//        B(d);
//     }
//     catch(MyException& e)
//     {
//        std::cerr << typeid(e).name() << '\n';
//     }
    
    
//  //   delete pd;
//     cout << "Exiting FunctionA" << endl;
// }

void handler(){
   cout << "in handler" << endl;
}

void f1(void) throw()
{
   cout << "About to throw 1" << endl;
   if(1)
      throw 1;
}

void f5(void)   
{
   try{
      f1();
   }
   catch(int e){
      cout << e << endl;
      handler();
   }
}

void f2(void){
   try
   {
      f1();
   }
   catch(int e)
   {
      cout << "f2:" << e << endl;
      handler();
   } 
}

extern "C" void f4(void);

void f4(void){
   f1();
}

int main()
{
   // f2();

   // try
   // {
   //    f4();
   // }
   // catch(...)
   // {
   //    cout << "Caught exception from f4" << endl;
   // }
   f5();   

   // cout << "Entering main" << endl;
   // Dummy d(" M");
   // A(d);
   // cout << "Exiting main." << endl;


   // Int a;
   // ++a;
   // a.show();

   // complex<int> c1(1,2);
   // complex<int> c2(2,3);
   // complex<int> c3 = c1+c2;
   // complex<int> c4 = c2-c1;

   // c1.show();
   // c3.show();
   // c4.show();

   // int *p = mynullptr;
   // int A::*a = mynullptr;
   // cout << p << endl;
   // cout << a << endl;

   //  IntVector v( 10 );
   // int i;

   // for( i = 0; i <= 10; ++i )
   //    v[i] = i;

   // v[3] = v[9];

   // for ( i = 0; i <= 10; ++i )
   //    cout << "Element: [" << i << "] = " << v[i] << endl;
    // constexpr CClass c1 = CClass(10);
    // constexpr CClass c2_6 = cube(c1);
    // void* p = nullptr;
    // int* pi = nullptr;
    // CClass c88(88);
    // cout << c88.n;

    // int s = 110;
    // analyze_string(s);

    // const int n = 12;
    // constexpr int N = calc(n);
    // cout << N << endl;

    // Foo1 sp;
}

// void analyze_string(int s)
// {
//     assert(s != 10);
// }