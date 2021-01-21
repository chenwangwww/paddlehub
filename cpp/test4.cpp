#include <iostream>
#include <fstream>
#include <exception>

using namespace std;

// class Box
// {
// private:
//     double width;

// public:
//     friend void printWidth(Box box);
//     void setWidth(double wid);
// };

// void Box::setWidth(double wid)
// {
//     width = wid;
// }

// void printWidth(Box box)
// {
//     cout << box.width << endl;
// }

extern int max(int a, int b);

class Distance
{
    private :
    int feet;
    int inches;
    public :
    Distance(){
        feet = 0;
        inches = 0;
    }
    Distance(int f, int i){
        feet = f;
        inches = i;
    }
    Distance operator()(int a, int b, int c)
    {
        Distance D;
        D.feet = a+c+10;
        D.inches = b+c+100;
        return D;
    }
    void displayDistance()
    {
        cout << feet << "," << inches << endl;
    }
};

class Adder{
    public:
    Adder(int i = 20){
        total = i;
    }
    void addFunc(int a){
        total += a;
    }
    int total;
};

struct MyException: public exception
{
    const char *what() const throw()
    {       
        return "c++ exception";
    }
};

void static_localVar()
{
    static int a = 0;
    cout << a << '\n';
    a++;
}

class Singleton
{
private:
    Singleton();
    ~Singleton();
    Singleton(const Singleton &);
    Singleton &operator=(const Singleton &);

private:
    static Singleton *instance;
    
public:
    static Singleton &Instance()
    {
        if(instance == nullptr)
            instance = new Singleton;
        return *instance;
    }

public:
    int val = 10;
};

Singleton* Singleton::instance = nullptr;
Singleton::Singleton()
{

}

class Box
{
public:
    Box(){
        cout << "调用构造函数！" << endl;
    }
    ~Box(){
        cout << "调用析构函数！" << endl;
    }

public:
    int sp = 1;
};

namespace first_space{
    void func(){
        cout << "Inside first_space" << endl;
    }

    namespace second_space{
        void func(){
            cout << "Inside second_space" << endl;
        }
    }
}

using namespace first_space;

int main()
{
    // Box box;
    // printWidth(box);
    // box.setWidth(10.45);
    // printWidth(box);

    // Distance D1(11, 10), D2;
    // D1.displayDistance();

    // D2 = D1(10,10,10);
    // D2.displayDistance();

    // Adder a;
    // a.addFunc(12);
    // cout << a.total;

    // char data[100];

    // ofstream outfile;
    // outfile.open("tt.txt");
    // cout << "Enter your name:";
    // cin >> data;

    // outfile << data << endl;

    // cout << "Enter your age:";
    // cin >> data;
    // cin.ignore();

    // outfile <<data << endl;

    // outfile.close();

    // ifstream infile;
    // infile.open("tt.txt");
    // cout << "name:";
    // infile >> data;
    // cout << data << endl;

    // infile >> data;
    // cout << data << endl;
    // infile.close();

    // fstream infile;
    // infile.open("tt.txt", ios::app | ios::out | ios::in);
    // char data[100];

    // infile << "dddata";
    // infile.seekg(ios::beg);
    // infile >> data;
    // cout << data;
    // infile.close();

    // try
    // {
    //     throw MyException();
    // }
    // catch(const MyException& e)
    // {
    //     std::cerr << e.what() << '\n';
    // }

    // double *pvalue = NULL;
    // pvalue = new double;

    // *pvalue = 29494.99;
    // cout << *pvalue;

    // delete pvalue;

    // static_localVar();
    // static_localVar();
    // static_localVar();

    // int ret = Singleton::Instance().val;
    // cout << ret;

    // void *c;
    // int *p = &a;
    // c = p;
    // double *q = nullptr;

    // int i,j,k;

    // int ***p;
    // p = new int **[2];
    // for (i = 0; i < 2; i++)
    // {
    //     p[i] = new int *[3];
    //     for (j = 0; j < 3; j++)
    //     {
    //         p[i][j] = new int[4];
    //     }
        
    // }
    
    // for (i = 0; i < 2; i++)
    // {
    //     for (j = 0; j < 3; j++)
    //     {
    //         for (k = 0; k < 4; k++)
    //         {
    //             p[i][j][k] = i+j+k;
    //             cout<<p[i][j][k]<<" ";
    //         }
    //         cout<<endl;
    //     }
    //     cout<<endl;
    // }

    // for (i = 0; i < 2; i++)
    // {
    //     for (j = 0; j < 3; j++)
    //     {
    //         delete [] p[i][j];
    //     }
        
    // }
    // for (i = 0; i < 2; i++)
    // {
    //     delete [] p[i];
    // }
    // delete [] p;
    
    // Box* mb = new Box[4];
    // cout << sizeof(char *) << endl;
    // delete[] mb;

    // cout << max(12,23);

    func();
    second_space::func();
}

