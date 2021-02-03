#include <iostream>
#include <string>
#include <memory>
using namespace std;

template<class Key, class Value> class Dictionary{
    Key* keys;
    Value* values;
    int size;
    int max_size;
public:
    Dictionary(int initial_size):size(0){
        max_size = 1;
        while (initial_size >= max_size)
        {
            max_size *= 2;
        }
        keys = new Key[max_size];
        values = new Value[max_size];
    }
    void add(Key key, Value value){
        Key* tmpKey;
        Value* tmpVal;
        if(size + 1 >= max_size){
            max_size *= 2;
            tmpKey = new Key[max_size];
            tmpVal = new Value[max_size];
            for (int i = 0; i < size; i++)
            {
                tmpKey[i] = keys[i];
                tmpVal[i] = values[i];
            }
            tmpKey[size] = key;
            tmpVal[size] = value;
            delete[] keys;
            delete[] values;
            keys = tmpKey;
            values = tmpVal;
        }
        else
        {
            keys[size] = key;
            values[size] = value;
        }
        size++;
    }

    void print()
    {
        for (int i = 0; i < size; i++)
        {
            cout << "{" << keys[i] << "," << values[i] << "}" << endl;
        }
        
    }
};

template<class Value> class Dictionary<int, Value>{
    int* keys;
    Value* values;
    int size;
    int max_size;
public:
    Dictionary(int initial_size): size(0){
        max_size = 1;
        while (initial_size >= max_size)
        {
            max_size *= 2;
        }
        keys = new int[max_size];
        values = new Value[max_size];
        
    }
    void add(int key, Value value){
        int* tmpKey;
        Value* tmpVal;
        if(size + 1 >= max_size){
            max_size *= 2;
            tmpKey = new int[max_size];
            tmpVal = new Value[max_size];
            for (int i = 0; i < size; i++)
            {
                tmpKey[i] = keys[i];
                tmpVal[i] = values[i];
            }
            tmpKey[size] = key;
            tmpVal[size] = value;
            delete[] keys;
            delete[] values;
            keys = tmpKey;
            values = tmpVal;
        }
        else
        {
            keys[size] = key;
            values[size] = value;
        }
        size++;
    }

    void sort()
    {
        int smallest = 0;
        for (int i = 0; i < size - 1; i++)
        {
            for(int j = i; j < size; j++)
            {
                if(keys[j] < keys[smallest])
                    smallest = j;
            }
            swap(keys[i], keys[smallest]);
            swap(values[i], values[smallest]);
        }
        
    }

    void print()
    {
        for (int i = 0; i < size; i++)
        {
            cout << "{" << keys[i] << "," << values[i] << "}" << endl;
        }
        
    }
};

struct Date
{
    short Month;
    short Day;
    short Year;
};

class DateTime
{
public:
    short Month;
    short Day;
    short Year;
};

class Point
{
    unsigned obj_x;
    unsigned obj_y;
public:
    unsigned& x();
    unsigned& y();
};

unsigned& Point::x()
{
    return obj_x;
}

unsigned& Point::y()
{
    return obj_y;
}

struct X{
    X(int i): m_i(i){}
    int m_i;
};

class LargetObject
{
public:
    void DoSth(){
        val = 12;
    }
public:
    int val;
};

void ProcessLargeObject(const LargetObject& lo){
    cout << lo.val << endl;
}

int main()
{
    unique_ptr<LargetObject> pLarge(new LargetObject());
    pLarge->DoSth();
    ProcessLargeObject(*pLarge);
    cout << pLarge.get() << endl;
    pLarge.reset();
    cout << pLarge.get() << endl;


    // const X cx(10);
    // const X* pcx = &cx;

    // X cx2(20);
    // X* const pcx2 = &cx2;

    // (*pcx2).m_i = 0;

    // int *const cpObject = 0;
    // int *pObject;
    // pObject = cpObject;
    // cout << cpObject << endl;
    // cout << pObject << endl;

    // Point thepoint;
    // thepoint.x() = 7;
    // thepoint.y() = 9;
    // cout << thepoint.x() << endl;
    // cout << thepoint.y() << endl;

    // Date date{8,27,2021};
    // cout << date.Year << date.Month << date.Day << endl;
    // DateTime date2{8,26,2020};
    // cout << date2.Year << date2.Month << date2.Day << endl;

    // Dictionary<string, string>* dict = new Dictionary<string, string>(10);
    // dict->add("apple", "fruit");
    // dict->add("banana", "fruit");
    // dict->add("dog", "animal");
    // dict->print();

    // Dictionary<int, string>* dict2 = new Dictionary<int, string>(10);
    // dict2->add(100, "apple");
    // dict2->add(101, "banana");
    // dict2->add(103, "dog");
    // dict2->add(89, "cat");
    // dict2->print();
    // dict2->sort();
    // cout << "sorted........" << endl;
    // dict2->print();
}