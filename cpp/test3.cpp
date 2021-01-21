#include <iostream>

using namespace std;

class Line
{
    public:
        void setLength(double len);
        double getLength(void);
        Line(double len);
        Line();
        ~Line();
    private:
        double length;
};

Line::Line()
{
    cout<<"Object is created."<<endl;
    length = 0;
}

Line::Line(double len)
{
    cout<<"Object is created."<<endl;
    length = len;
}

Line::~Line()
{
    cout<<"Object is deleted."<<endl;
}

void Line::setLength(double len)
{
    length = len;
}

double Line::getLength(void)
{
    return length;
}

class Dis
{
private:
    bool sp;
    int item;
public:
    Dis(bool s);
    ~Dis();
    void showBool();
    Dis operator!();
    Dis operator+(const Dis& b);
};

Dis::Dis(bool s)
{
    sp = s;
    item = 1;
}

Dis::~Dis()
{
}

void Dis::showBool()
{
    cout<<sp<<","<<item<<endl;
}

Dis Dis::operator!()
{
    Dis ss = Dis(!sp);
    return ss;
}

Dis Dis::operator+(const Dis& b)
{
    Dis ret = Dis(b.sp);
    ret.item = this->item + b.item;
    return ret;
}

int main()
{
    // Line line;
    // cout<<line.getLength()<<endl;
    // line.setLength(4.7);
    // cout<<line.getLength()<<endl;

    Dis a = Dis(false);
    a.showBool();
    a = !a;
    a.showBool();
    Dis c = a + Dis(false);
    c.showBool();

    return 0;
}