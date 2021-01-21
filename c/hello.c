#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include "hello.h"

// extern int errno;
extern int val;
int x, y;
int addtwonum()
{
    x = 1, y = 2;
    return x + y;
}

#define LENGTH 10
#define WIDTH 5
#define CC '\t'

#define tokenpaster(n) printf("token"#n"=%d", token##n)
#if !defined(MESSAGE)
    #define MESSAGE "you wish!"
#endif

#define MAX(x,y) ((x) > (y) ? (x) : (y))

int g = 200;
void func1(void);
static int count=10;
// int max(int, int);

void populate_array(int *array, size_t arraySize, int(*getNextValue)(void))
{
    for (size_t i = 0; i < arraySize; i++)
    {
        array[i] = getNextValue();
    }
    
}
int getNextRandomValue()
{
    return rand();
}

struct Books
{
    char title[50];
    char author[50];
    char subject[100];
    int book_id;
};
void printBook(struct Books book);

typedef struct
{
    unsigned int age:3;
} Age;

double factorial(unsigned int i)
{
    if(i <= 1)
    {
        return 1;
    }
    return i * factorial(i - 1);
}

int main(int argc, char* argv[])
{
    // printf("hello, world!");

    // printf("%d", sizeof(long long));
    // printf("%d", val);

    // double d = 3.84;
    // int i = (int)d;
    // printf("%d", i);

    // int result;
    // result = addtwonum();
    // printf("result is %d", result);
    
    // int area;   
    // area = LENGTH * WIDTH;
    // printf("%d%d", area, area);

    // while (count--)
    // {
    //     func1();
    // }

    // double xx = 5.3;
    // xx--;
    // printf("%.3f", xx);
    
    // int i = 56;
    // printf("%#X", i);

    // int* a = &x;
    // printf("%d, %d, %d", x, &x==a, *a);

    // int a = 1;
    // for (; a > 0; a++)
    // {
    //     printf("%d", a);
    // }  

    // int a = 100;
    // int b = 200;
    // int ret;
    // ret = max(a, b);
    // printf("%d", ret);

    // printf("%d", g);

    // int vv;
    // int b = ++vv;
    // printf("%d", b);

    // double balance[] = {100.0, 2.0, 3.4, 4.5, 56.0};
    // printf("%d, %f, %d, %f", &(balance[1]), balance[1], &(balance[2]), balance[2]);
    // printf("%d, %d", balance, &(balance[0]));

    // int a;
    // scanf("%u", &a);
    // printf("%u", a);

    // enum Day
    // {
    //     saturday, sunday, monday
    // }day;
    // day = sunday;
    // printf_s("%d", day);

    // double balance[] = {100.0, 2.0, 3.4, 4.5, 56.0};
    // printf("%#X, %f, %#X, %f", &(balance[1]), balance[1], &(balance[2]), balance[2]);

    // int* ptr = &g;
    // printf("%p, %d", ptr, *ptr);

    // int *p = malloc(sizeof(int));
    // printf("%p", p);

    // int *p = malloc(sizeof*p);
    // *p = 10;
    // free(p);
    // printf("%p, %d", p, *p);

    // int a = 10;
    // int *p = &a;
    // free(p);
    // printf("%d", *p);

    // int myarray[10];
    // populate_array(myarray, 10, getNextRandomValue);
    // for (size_t i = 0; i < 10; i++)
    // {
    //     printf("%d, ", myarray[i]);
    // }
    
    // char pstr[] = {'H', 'e', 'l', 'l', 'o', '\0'};
    // printf("%d", strlen(pstr));

    // typedef struct 
    // {
    //     int a;
    //     char b;
    // } Sim;
    // Sim s1;
    // s1.a = 10, s1.b = 'f';

    // struct Books Book1;
    // strcpy(Book1.title, "C Programming");
    // strcpy(Book1.author, "Nuha Ali");
    // strcpy(Book1.subject, "C Programming Tutorial");
    // Book1.book_id = 6495407;
    // printBook(Book1);

    // struct bs{
    //     unsigned a:1;
    //     unsigned b:3;
    //     unsigned c:4;
    // } bit, *pbit;
    // bit.a = 1;
    // bit.b = 7;
    // bit.c = 15;
    // printf("%d,%d,%d\n", bit.a, bit.b, bit.c);
    // pbit = &bit;
    // pbit->a = 0;
    // pbit->b &= 3;
    // pbit->c |= 1;
    // printf("%d,%d,%d\n", pbit->a, pbit->b, pbit->c);

    // union Data
    // {
    //     int i;
    //     float f;
    //     char str[20];
    // };
    // typedef union Data dd;
    // dd data;
    // printf("%d", sizeof(dd));

    // char str[20];
    // printf("%#x\n", str);
    // strcpy(str, "program");
    // printf("%#x", str);

    // Age a;
    // a.age = 4;
    // printf("%d\n", sizeof(a));
    // printf("%d\n", a.age);
    // a.age = 8;
    // printf("%d", a.age);

    // int c;
    // printf("Enter a value:");
    // c = getchar();
    // printf("\nyou entered:");
    // putchar(c);
    // printf("\n%d", c);

    // char str[100];
    // printf("Enter a value:");
    // gets(str);
    // printf("\nyou entered:");
    // puts(str);
    // printf("end!");

    // printf("%d", EOF);

    // FILE *fp = NULL;
    // fp = fopen("./test.txt", "w+");
    // fprintf(fp, "this is the first line!\n");
    // fputs("this is the second line!\n", fp);
    // fclose(fp);

    // FILE *fp = NULL;
    // char buff[255];
    // fp = fopen("test.txt", "r");
    // fscanf(fp, "%s", buff);
    // printf("1: %s\n", buff);
    // fgets(buff, 255, fp);
    // printf("2: %s\n", buff);
    // fgets(buff, 255, fp);
    // printf("3: %s\n", buff);
    // fclose(fp);

    // printf("%s", __FILE__);
    // printf("%s", __DATE__);
    // printf("%s", __TIME__);

    // int token34 = 40;
    // tokenpaster(34);

    // printf("here is the message:%s\n", MESSAGE);

    // printf("Max between 20 and 10 is %d\n", MAX(10, 20));
    // int arr[2] = {1,2};
    // int *p = arr;
    // printf("%#x\n", p);
    // p++;
    // printf("%#x", p);
    // printf("%d", sizeof(long long));

    // FILE *pf;
    // int errnum;
    // pf = fopen("aa.txt", "r");
    // if(pf == NULL)
    // {
    //     errnum = errno;
    //     fprintf(stderr, "error number: %d\n", errno);
    //     perror("perror!");
    //     fprintf(stderr, "openfile error:%s\n", strerror(errnum));
    // }else
    // {
    //     fclose(pf);
    // }
    
    // int i = 5;
    // printf("%d:%f", i, factorial(i));

    // int b = Max2(20, 13);
    // printf("%d", b);
    /*
    int a;
    int b;
    */

    // int b = unsafe(-10);
    // printf("%2d", b);

    // char *s = "111";
    // printf("%p\n", s);
    // printf("%p", &"111");

    // int a = 2;
    // double dd = 200.2;
    // void *c;
    // int *p = &a;
    // c = p;
    // double *q = c;
    // q = &dd;
    // printf("%.f", *q);

    // int *s1 = &a;
    // char *sp;
    // void *v1;
    // double *d1;
    // printf("%d, %d, %d, %d", sizeof(s1), sizeof(v1), sizeof(d1), sizeof(sp));

    // char *s1 = "hello world";
    // printf("%#x", s1);

    return 0;
}

void printBook(struct Books book)
{
    printf("Book title : %s\n", book.title);
    printf("Book author : %s\n", book.author);
    printf("Book subject : %s\n", book.subject);
    printf("Book book_id : %d\n", book.book_id);
}

int sum(int a, int b);

void func1(void)
{
    static  int th = 5;
    th++;
    printf("th is %d, count is %d\n", th, count);
}


