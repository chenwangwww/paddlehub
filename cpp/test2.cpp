#include <iostream>
#include <ctime>
#include <cstdlib>
#include <cstring>

using namespace std;
void getSeconds(unsigned long *par);

int *getRandom()
{
    static int r[3];
    srand((unsigned)time(NULL));
    for (int i = 0; i < 3; i++)
    {
        r[i] = rand();
        cout<<r[i]<<endl;
    }
    return r;
}

void swap(int& x, int& y);

#define BST (+1)
#define CCT (+8)

void printBook( struct Books book );

 
// 声明一个结构体类型 Books 
struct Books
{
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
};

void modifyBook( struct Books *book )
{
   book->book_id = 10000;
}

int main()
{
    // unsigned long sec;
    // getSeconds(&sec);
    // cout<<sec;

    // int *p;
    // p =  getRandom();
    // for (int i = 0; i < 3; i++)
    // {
    //     cout<<*(p+i)<<endl;
    // }

    // int a = 100, b = 200;
    // swap(a,b);
    // cout<<a<<endl;
    // cout<<b<<endl;

    // time_t now = time(0);
    // tm *ltm = localtime(&now);
    // cout<<ltm->tm_year<<endl;
    // cout<<ltm->tm_mon<<endl;
    // cout<<ltm->tm_mday<<endl;
    // cout<<ltm->tm_hour<<":"<<ltm->tm_min<<":"<<ltm->tm_sec<<endl;
    // cout<<ctime(&now)<<endl;

    // time_t rawtime;
    // struct tm *info;

    // time(&rawtime);
    // info = gmtime(&rawtime);
    // printf("%02d:%02d\n", (info->tm_hour+BST)%24, info->tm_min);
    // printf("%2d:%02d\n", (info->tm_hour+CCT)%24, info->tm_min);

    // const char *s = "111";
    // char s2[] = "111";
    // printf("%p\n", s);
    // printf("%p\n", &"111");
    // printf("%p", s2);

    // time_t rawtime;
    // struct tm *info;
    // char buffer[80];

    // time(&rawtime);
    // info = localtime(&rawtime);
    // strftime(buffer, 80, "%Y-%m-%d %H:%M:%S", info);
    // printf("%s", buffer);

    // char name[50];
    // int age;
    // cout<<"input your name and age.\n";
    // cin>>name>>age;
    // cout<<name<<endl;
    // cout<<age+1<<endl;

    // clog<<"error message";

    Books Book1; // 定义结构体类型 Books 的变量 Book1

    // Book1 详述
    strcpy(Book1.title, "C++ 教程");
    strcpy(Book1.author, "Runoob");
    strcpy(Book1.subject, "编程语言");
    Book1.book_id = 12345;
    printBook( Book1 );
    modifyBook(&Book1);
    printBook( Book1 );
}

void getSeconds(unsigned long *par)
{
    *par = time(NULL);
}

void swap(int& x, int& y)
{
    int temp;
    temp = x;
    x = y;
    y = temp;
}

void printBook( struct Books book )
{
   cout << "书标题 : " << book.title <<endl;
   cout << "书作者 : " << book.author <<endl;
   cout << "书类目 : " << book.subject <<endl;
   cout << "书 ID : " << book.book_id <<endl;
}